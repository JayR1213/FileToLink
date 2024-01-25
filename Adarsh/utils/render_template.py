from Adarsh.vars import Var
from Adarsh.bot import StreamBot
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.file_properties import get_file_ids
from Adarsh.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp


async def render_page(id, secure_hash):
    file_data=await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    
    if str(file_data.mime_type.split('/')[0].strip()) == 'video':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Watch {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    elif str(file_data.mime_type.split('/')[0].strip()) == 'audio':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Listen {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    else:
        async with aiofiles.open('Adarsh/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    heading = 'Download {}'.format(file_data.file_name)
                    file_size = humanbytes(int(u.headers.get('Content-Length')))
                    html = (await r.read()) % (heading, file_data.file_name, src, file_size)
    current_url = f'{Var.URL}/{str(id)}/{file_data.file_name}?hash={secure_hash}'
    html_code = f'''
<p>
<center><h4>Click On 👇 Button To Watch/Download In Your Favorite Player</h4></center>
<center>
    <button style="font-size: 18px; width: 130px; height: 40px; cursor: pointer; background-color: rgb(0, 4, 255); color: #FFFFFF; border-radius: 10px;" onclick="window.location.href = 'intent:{current_url}#Intent;package=com.mxtech.videoplayer.ad;S.title={file_data.file_name};end'"><b>MX Player</b></button>&nbsp &nbsp
    <button style="font-size: 18px; width: 130px; height: 40px; cursor: pointer; background-color: rgb(255, 85, 0); color: #FFFFFF; border-radius: 10px;" onclick="window.location.href = 'vlc://{current_url}'"><b>VLC Player</b></button>&nbsp &nbsp
    <br><br>
    <button style="font-size: 18px; width: 130px; height: 40px; cursor: pointer; background-color: rgb(104, 3, 255); color: #FFFFFF; border-radius: 10px;" onclick="window.location.href = `intent:{current_url}#Intent;action=com.young.simple.player.playback_online;package=com.young.simple.player;end`"><b>S Player</b></button>&nbsp &nbsp
    <button style="font-size: 18px; width: 130px; height: 40px; cursor: pointer; background-color: rgb(255, 0, 0); color: #FFFFFF; border-radius: 10px;" onclick="window.location.href = 'playit://playerv2/video?url={current_url}&amp;title={file_data.file_name}'"><b>Playit Player</b></button>&nbsp &nbsp
    <br><br>
    <button style="font-size: 20px; width: 180px; height: 45px; cursor: pointer; background-color: rgb(0, 137, 25); color: #FFFFFF; border-radius: 10px;" onclick="window.location.href = '{current_url}'"><b>Download Now</b></button> &nbsp &nbsp
    <br><br>
    <a style="text-decoration: none;" href="https://telegram.dog/+YzxA0sElhW41MDBl">
        <button style="font-size: 17px; width: 140px; height: 40px; cursor: pointer; background-color: rgb(9, 0, 139); color: #ffffff; border-radius: 10px;"><b>JOIN NOW</b></button>&nbsp &nbsp
    </a>
</center>
<br>

'''

    html += html_code    
    return html
