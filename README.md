# Brew GUI
macOS 专用 Homebrew 图形化管理工具，基于 CustomTkinter 开发，不用敲终端命令，图形界面操作 Homebrew。

## ✨ 功能特点
- 图形界面完成软件包**安装、更新、卸载**
- 支持更新 Homebrew 自身
- 查看已安装的 brew 应用列表
- 界面简洁，操作直观，配套 macOS 一键依赖脚本

## 📦 发布资源 Assets 说明
| 文件名称 | 适用平台 | 说明 |
|--------|--------|------|
| install_dependencies.sh | macOS | Mac 依赖安装脚本 |
| Brew-GUI-macos-v0.1.dmg | macOS | macOS 标准安装镜像，拖拽至应用程序即可使用 |
| Brew-GUI-linuxormacos-v0.1.zip | macOS / Linux | macOS 绿色压缩包，解压后直接运行 |

## 📖 使用教程
### 方式一：运行编译好的程序包
1. 进入仓库 Releases 页面，下载对应 macOS 程序文件
2. 运行对应程序：
- Mac DMG：打开镜像文件，将软件拖入「应用程序」文件夹
- Mac 压缩包：解压压缩包，运行内部可执行文件

> ⚠️ 前提条件：你的 Mac 设备上**必须预先安装好 Homebrew**，本工具仅为图形外壳，不会自动安装 Homebrew。

### 方式二：源码运行
1. 下载源码到本地文件夹
2. 终端执行安装依赖脚本：
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. 启动程序
```bash
python main.py
```

## ⚠️ 注意事项
1. 本机需要预先安装 Homebrew，并且终端可以正常执行 `brew` 命令
2. 需要 Python 环境并配置好环境变量
3. 运行shell脚本前需要赋予执行权限
4. 部分软件安装、卸载可能需要终端密码授权
5. 部分软件安装、卸载可能需要终端密码授权
6. 部分软件安装、卸载可能需要终端密码授权

## 项目信息
- 项目名称：Brew GUI
- 工具系列：QPALZM Toolkit
- 开发作者：AdkSetup
- 支持平台：macOS/Linux

