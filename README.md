# Brew GUI

macOS / Linux 图形化 Homebrew 管理工具，基于 CustomTkinter 开发，无需敲终端命令。

A graphical Homebrew manager for macOS and Linux, built with CustomTkinter — manage packages without touching the terminal.

---

[中文文档](#中文文档) | [English Documentation](#english-documentation)

---

<a id="中文文档"></a>

## 为什么选择 Brew GUI？

Homebrew 是 macOS 和 Linux 上最常用的包管理器，但大多数时候仍然需要在终端里敲命令。Brew GUI 把它包进了一个干净的图形界面——安装、更新、卸载，全部用按钮完成。

核心优势：

- 🖥️ **纯图形界面**：安装、更新、卸载全部通过按钮操作，无需记忆任何命令
- 🔄 **支持 Homebrew 自身更新**：一键更新，保持包管理器最新
- 📋 **已安装应用列表**：图形化查看当前已安装的 brew 包
- 🍎 **macOS 原生体验**：使用 CustomTkinter 构建，界面简洁、适配 macOS 视觉风格
- 🐧 **双平台支持**：macOS 与 Linux 均可运行（依赖系统已安装 Homebrew）

## 环境要求

> ⚠️ **前提条件**：你的设备上**必须预先安装好 Homebrew**，本工具仅为图形外壳，不会自动安装 Homebrew。

- macOS 或 Linux 系统
- 已安装的 Homebrew（终端执行 `brew --version` 可验证）
- Python 3 环境，并配置好系统环境变量

## 安装依赖

本项目依赖：

- `customtkinter`
- `termcolor`

**一键安装脚本（推荐）：**

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

**手动安装：**

```bash
pip install customtkinter termcolor
```

## 使用教程

### 方式一：运行编译好的程序包

1. 进入仓库 [Releases](../../releases) 页面，下载对应平台的程序文件
2. 运行对应程序：
   - **macOS DMG**：打开镜像文件，将软件拖入「应用程序」文件夹
   - **macOS / Linux 压缩包**：解压压缩包，运行内部可执行文件

### 方式二：源码运行

1. 克隆仓库

```bash
git clone https://github.com/adksetup/Brew-GUI.git
cd Brew-GUI
```

2. 安装依赖（二选一）

```bash
chmod +x install_dependencies.sh && ./install_dependencies.sh
```

或手动执行：

```bash
pip install customtkinter termcolor
```

3. 启动程序

```bash
python main.py
```

## 发布资源 Assets 说明

| 文件名称 | 适用平台 | 说明 |
|--------|--------|------|
| `install_dependencies.sh` | macOS / Linux | 依赖一键安装脚本 |
| `Brew-GUI-macos-v0.1.dmg` | macOS | macOS 标准安装镜像，拖拽至应用程序即可使用 |
| `Brew-GUI-linuxormacos-v0.1.zip` | macOS / Linux | 绿色压缩包，解压后直接运行 |

## 功能操作说明

| 功能 | 对应命令 | 说明 |
|------|---------|------|
| 安装 | `brew install` | 输入包名后点击「安装」 |
| 更新 | `brew upgrade` | 输入包名后点击「更新」 |
| 卸载 | `brew uninstall` | 输入包名后点击「卸载」 |
| 更新 Brew | `brew update` | 更新 Homebrew 自身 |
| 应用列表 | `brew list` | 查看已安装的 brew 应用 |

## 注意事项

1. 本机需要预先安装 Homebrew，并且终端可以正常执行 `brew` 命令
2. 需要 Python 环境并配置好系统环境变量
3. 运行 shell 脚本前需要赋予执行权限（`chmod +x`）
4. 部分软件安装、卸载可能需要终端密码授权
5. 命令通过 shell 执行，请自行确认输入的包名是否正确

## 项目信息

- 项目名称：Brew GUI
- 工具系列：QPALZM Toolkit
- 开发作者：AdkSetup/JC5
- 支持平台：macOS / Linux

## 开源协议

本项目基于 [MIT License](./LICENSE) 开源。

---

<a id="english-documentation"></a>

## Why Brew GUI?

Homebrew is the most popular package manager on macOS and Linux, but most of the time you still have to type commands in a terminal. Brew GUI wraps it in a clean graphical interface — install, update, and uninstall, all with buttons.

Key features:

- 🖥️ **Pure GUI**: Install, update, and uninstall via buttons — no commands to memorize
- 🔄 **Homebrew self-update**: Keep the package manager current with one click
- 📋 **Installed package list**: View installed brew packages graphically
- 🍎 **Native macOS feel**: Built with CustomTkinter — clean interface matching macOS aesthetics
- 🐧 **Cross-platform**: Runs on both macOS and Linux (requires Homebrew to be installed)

## Requirements

> ⚠️ **Prerequisite**: Homebrew **must already be installed** on your system. This tool is only a graphical shell and will not install Homebrew for you.

- macOS or Linux
- Homebrew installed (verify with `brew --version`)
- Python 3 with the system `PATH` configured

## Install Dependencies

This project depends on:

- `customtkinter`
- `termcolor`

**One-click installer (recommended):**

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

**Manual install:**

```bash
pip install customtkinter termcolor
```

## Usage

### Option 1: Run the packaged binary

1. Go to the repository's [Releases](../../releases) page and download the file for your platform.
2. Run it:
   - **macOS DMG**: open the disk image and drag the app into **Applications**
   - **macOS / Linux archive**: extract the archive and run the included executable

### Option 2: Run from source

1. Clone the repository

```bash
git clone https://github.com/adksetup/Brew-GUI.git
cd Brew-GUI
```

2. Install dependencies (pick one)

```bash
chmod +x install_dependencies.sh && ./install_dependencies.sh
```

Or manually:

```bash
pip install customtkinter termcolor
```

3. Launch the program

```bash
python main.py
```

## Release Assets

| File Name | Platform | Description |
|-----------|----------|-------------|
| `install_dependencies.sh` | macOS / Linux | One-click dependency installer |
| `Brew-GUI-macos-v0.1.dmg` | macOS | Standard macOS disk image — drag to Applications |
| `Brew-GUI-linuxormacos-v0.1.zip` | macOS / Linux | Portable archive — extract and run directly |

## Operations

| Operation | Command | Description |
|-----------|---------|-------------|
| Install | `brew install` | Enter a package name and click "Install" |
| Update | `brew upgrade` | Enter a package name and click "Update" |
| Uninstall | `brew uninstall` | Enter a package name and click "Uninstall" |
| Update Brew | `brew update` | Update Homebrew itself |
| Package list | `brew list` | View installed brew packages |

## Notes

1. Homebrew must be pre-installed and `brew` must be runnable from the terminal.
2. Python must be installed and added to your system `PATH`.
3. Remember to grant execute permission to the shell script before running (`chmod +x`).
4. Installing or uninstalling some packages may require terminal password authorization.
5. Commands are executed through the shell — please double-check the package name you enter.

## Project Info

- Name: Brew GUI
- Series: QPALZM Toolkit
- Author: AdkSetup/JC5
- Supported platforms: macOS / Linux

## License

Released under the [MIT License](./LICENSE).