## 呐~Yuki~

您的群组服操作小助手。

使用Python3编写。使用 **.yaml** 配置文件记录子服，配合Screen管理Linux系统上的Minecraft子服，支持MCDR子服与非MCDR子服。

### 功能：

 1. 开启所有子服

 2. 关闭所有子服

 3. 重载所有子服MCDR

 4. 重载所有子服ChatBridge

    

### 使用方法：

1. #### 安装Screen

   使用前请确保您系统中装有Screen，Linux系统下可以使用如下命令安装：

   ##### 	CentOS7/8：

   ```
   yum install screen
   ```

   ##### 	Ubentu/Debian：

   ```
   apt-get install screen
   ```

   ##### 	FreeBSD：

   ```
   pkg install screen
   ```

​		注意：安装过程中数据校验需要输入 '**y**' 以继续安装。

2. #### 安装Python依赖：

   ```
   pip3 install –r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

3. #### 根据.yaml文件内提示添加子服信息

   

4. #### 给程序添加可执行权限：

   ```
   chmod 750 nayuki.py
   ```

5. #### 于当前目录下使用yuki ，观察控制台输出测试程序是否正常运行：

   ```
   python nayuki.py
   ```

​		如：![print_output](https://github.com/Sinbing/Na-Yuki/blob/main/png/print_output.png)

 6. #### 正常运行后，修改程序Debug模式，正式使用：

    修改第20行内容：

    ```
    DEBUG_FLAG = True
    
    修改为
    
    DEBUG_FLAG = False
    ```

    

### 特别说明

在程序制作过程中没有任何yuki受到除血压以外的伤害。

