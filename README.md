# Cam-Scan

![Screenshot from 2021-08-02 05-55-49](https://user-images.githubusercontent.com/54572947/127843607-bfceeb77-52da-4d90-b686-a04d992be963.png)


# About
* Runs massscan on the input file containg ips or subnets
* Creates a file with desired port with masscan and send it to cameradar to find cameras
* After getting cameras, it creates a list of cameras urls and send it to take screenshots
 

# Requirements

It requires python 2.X and works only on Linux
```
apt install docker
apt install ffmpeg
pip install multiprocessing.dummy
pip install netaddr
pip install masscan

```
# Usage

Save ip/subnets list in a single file and run the following command

```python cam-scan.py iplist threads_count```

### Example
```python cam-scan.py iplist 10```

# Output Result
### Created separate XML and HTML folders



### File Names



### HTML result displayed in browser




Special Thanks to Cameradar developers https://github.com/Ullaakut/cameradar

