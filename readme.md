# 【copylot】Photoshop的实时stable diffusion插件！

大家有用过Github Copilot吗？Github Copilot可以在你写代码的时候，帮你把你不会写或者懒得写的部分直接写出来。

如果画画的时候也有copilot帮我画就好了！

于是聪明的莉沫酱发明了1个Photoshop的插件，叫copylot！它可以像Github Copilot那样实时帮你把你的画补充完整！


## 示例视频

[好.webm](https://github.com/RimoChan/copylot/assets/20064807/92e052ef-5402-4c55-8f0d-4f80ebae1b05)


## 使用方法

- 首先你需要1个Python和1个Photoshop。(我已经换Python 3.11了所以不知道最低版本号是多少)

- 安装1个[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)。运行webui-user.bat时，启动参数需要加上--api才能从API访问。

- 给stable-diffusion-webui下载1个[LCM-LORA](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5)，可以大幅减少图像生成所需的steps以加快生成速度，不过模型的画风也会有1些改变……不用也行。

- 把这个仓库clone回去，然后运行`pip install requirements.txt`。

- 运行`python copylot.py`就可以了。运行参数都写在代码里，直接改掉就可以了，不过调用stable diffusion API的参数是写在`设置文件`里的，这部分参数在运行时可以动态刷新。


## 已知bug

由于这个插件的实现非常奇怪，所以可能出现各种异常。

比如Photoshop突然鬼畜，发出异响什么的，都是正常的……


## 结束

就这样，大家88，我要回去报考维也呐艺术学院了！
