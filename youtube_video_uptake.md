
```
```python
import pafy
url ='https://www.youtube.com/watch?v=jk7AQ_B3qTU'
video = pafy.new(url)
```


```python
#get certain attributes:
video.title
```



```
'Caterpillar and Uptake to Create Analytics Solutions'
```



```python
video.rating
```




    4.84615373611




```python
video.viewcount, video.author, video.length
```




    (7958, 'Caterpillar Inc.', 165)




```python
video.duration, video.likes, video.dislikes
```




    ('00:02:45', 25, 1)




```python
print(video.description)
```

    http://caterpillar.com/ - Big Iron. Big Data. Learn how Caterpillar and Uptake will jointly develop an end-to-end platform for predictive diagnostics to help Caterpillar customers monitor and optimize their fleets more effectively.
    


```python
#list available streams for a video:
streams = video.streams
```


```python
for s in streams:
    print(s)
```

    normal:3gp@176x144
    normal:3gp@320x240
    normal:flv@400x240
    normal:webm@640x360
    normal:mp4@640x360
    


```python
#show all formats, file-sizes and their download url:
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)
```

    176x144 3gp 1690388 https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2F3gpp&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=2F3A544D3DF2750623D1B56B6B1071CA30F9DC60.C6BD220A4028ADF7605995AE7C06DB840CCFAF3A&requiressl=yes&dur=164.304&source=youtube&lmt=1425502521486449&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=17&ratebypass=yes
    320x240 3gp 4680688 https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2F3gpp&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=DF81FC336255504981C2A5D320CAB00296F5BA50.CCA2565759C1C8759EAA598A688E819CFC12F28F&requiressl=yes&dur=164.257&source=youtube&lmt=1425502546916176&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=36&ratebypass=yes
    400x240 flv 7021129 https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fx-flv&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=7E3844FF7C716B823F88B66147E619B4C559B341.372C178BDF4D2D8ED2ADA0CF6EE4DF79D10C47EF&requiressl=yes&dur=164.101&source=youtube&lmt=1425502443596470&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=5&ratebypass=yes
    640x360 webm 14713663 https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fwebm&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=8E01A63FBCBDC6BA71771A7933E611E04D9BB0C6.A2BD8DD14FC45DD9F31158B585C9894DD93A6408&requiressl=yes&dur=0.000&source=youtube&lmt=1425503030733913&ratebypass=yes&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=43
    640x360 mp4 11865905 https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fmp4&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=D3DA67AB3E246519715B4B614648232DC3DF6EA6.4D7924367B3346E2EF87E9715886AF854238CEE2&requiressl=yes&dur=164.118&source=youtube&lmt=1427445810118638&ratebypass=yes&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=18
    


```python
 best = video.getbest()
```


```python
#get best resolution regardless of file format:
best.resolution, best.extension
```




    ('640x360', 'webm')




```python
#get best resolution for a particular file format (mp4, webm, flv or 3gp):
best = video.getbest(preftype="webm")
best.resolution, best.extension
```




    ('640x360', 'webm')




```python
#get url, for download or streaming in mplayer / vlc etc:
best.url
```




    'https://r4---sn-p5qlsnzd.googlevideo.com/videoplayback?mn=sn-p5qlsnzd&mm=31&id=o-AFrJPJ4TMVGon5kJNDuIeUXlEHtr8aoEX0IKvK8wViMo&ip=75.102.136.35&pl=24&mv=m&mt=1451171769&ms=au&ipbits=0&initcwndbps=2331250&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fwebm&fexp=9414672%2C9416126%2C9417828%2C9417893%2C9420095%2C9420452%2C9422596%2C9423662%2C9424127%2C9424624%2C9425057%2C9425960%2C9426009%2C9426048&nh=IgpwcjAxLmlhZDA3KgkxMjcuMC4wLjE&key=yt6&signature=8E01A63FBCBDC6BA71771A7933E611E04D9BB0C6.A2BD8DD14FC45DD9F31158B585C9894DD93A6408&requiressl=yes&dur=0.000&source=youtube&lmt=1425503030733913&ratebypass=yes&expire=1451193484&upn=ymELLnsoXpQ&sver=3&itag=43'




```python
#Get audio-only streams (m4a and/or ogg vorbis):
audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())
```

    50k webm 991767
    70k webm 1309486
    128k webm 2243051
    128k m4a 2635426
    160k webm 3247126
    256k m4a 5233120
    

```
