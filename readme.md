# 【copylot】Photoshop实时stable diffusion插件

大家有用过Github Copilot吗？Github Copilot可以在你写代码的时候，帮你把你不会写或者懒得写的部分直接写出来。

如果画画的时候也有copilot帮我画就好了！

于是聪明的莉沫酱发明了1个Photoshop的插件，叫copylot！它可以像Github Copilot那样实时帮你把你的画补充完整！


## 示例视频



## 使用方法

- 首先你需要1个Python和1个Photoshop。(我已经换Python 3.11了所以不知道最低版本号是多少)

- 安装1个[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)。运行webui-user.bat时，启动参数需要加上--api才能从API访问。

- 给stable-diffusion-webui下载1个[LCM-LORA](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5)，可以大幅减少图像生成所需的steps以加快生成速度，不过模型的画风也会有1些改变……不用也行。

- 把这个仓库clone回去，然后运行`pip install requirements.txt`。

- 运行`python copylot.py`。运行参数都写在代码里，直接改掉就可以了，不过调用stable diffusion API的参数是写在`设置文件`里的，这部分参数在运行时可以动态刷新。


## 结束

就这样，大家88，我要回去报考维也纳艺术学院了！
