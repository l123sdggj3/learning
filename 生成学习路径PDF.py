# -*- coding: utf-8 -*-
"""生成《管道爬行切断装置 关键学习路径》PDF"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)

# ---------- 字体 ----------
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("SimHei", os.path.join(FONT_DIR, "simhei.ttf")))
pdfmetrics.registerFont(TTFont("Deng", os.path.join(FONT_DIR, "Deng.ttf")))
pdfmetrics.registerFont(TTFont("KaiTi", os.path.join(FONT_DIR, "simkai.ttf")))

# ---------- 颜色 ----------
PRIMARY = colors.HexColor("#1F4E79")   # 深蓝
ACCENT = colors.HexColor("#2E75B6")    # 亮蓝
GRAY = colors.HexColor("#595959")
LIGHT = colors.HexColor("#EEF3F8")
WARN = colors.HexColor("#B00020")

# ---------- 样式 ----------
st_title = ParagraphStyle("title", fontName="SimHei", fontSize=23, leading=30,
                          alignment=TA_CENTER, textColor=PRIMARY, spaceAfter=6)
st_sub = ParagraphStyle("sub", fontName="Deng", fontSize=11, leading=16,
                        alignment=TA_CENTER, textColor=GRAY, spaceAfter=14)
st_h1 = ParagraphStyle("h1", fontName="SimHei", fontSize=14, leading=19,
                       textColor=PRIMARY, spaceBefore=14, spaceAfter=6)
st_h2 = ParagraphStyle("h2", fontName="SimHei", fontSize=11.5, leading=16,
                       textColor=ACCENT, spaceBefore=8, spaceAfter=3)
st_body = ParagraphStyle("body", fontName="Deng", fontSize=10, leading=16,
                         alignment=TA_JUSTIFY, textColor=colors.HexColor("#222222"),
                         spaceAfter=2)
st_bullet = ParagraphStyle("bullet", parent=st_body, leftIndent=12,
                           bulletIndent=2, spaceAfter=2)
st_note = ParagraphStyle("note", parent=st_body, textColor=WARN, fontName="SimHei",
                         fontSize=9.5)

def P(text, style=st_body):
    return Paragraph(text, style)

def B(text):
    return Paragraph(text, st_bullet, bulletText="•")

def H1(text):
    return Paragraph(text, st_h1)

def H2(text):
    return Paragraph(text, st_h2)

# ---------- 内容 ----------
story = []

story.append(P("管道爬行 · 切断一体化无人装置", st_title))
story.append(P("关键学习路径 —— Arduino 控制 + 传感器检测 + 机械执行（无人化“检测→判断→执行”闭环）", st_sub))
story.append(HRFlowable(width="100%", thickness=1.2, color=PRIMARY, spaceAfter=6))

# 一、概述
story.append(H1("一、项目概述与目标"))
story.append(P("本装置需同时具备以下能力：① 套在管子上沿管滚动（爬行）；② 切断管子；"
              "③ 距离、温度等传感检测；④ 由内部电路（Arduino）控制；⑤ 无人化——检测到目标后自动执行相应操作。"))
story.append(P("建议整体按“先仿真验证电路 → 面包板搭接 → 机械样机 → 整机联调”的顺序推进，"
              "避免一开始就投入机械加工导致返工。学习路径如下，可对照阶段逐项完成。"))

# 二、架构
story.append(H1("二、系统总体架构（五大子系统）"))
for t in ["<b>机械子系统</b>：环形抱管 + 滚轮爬行机构、切断执行机构、夹持/锁紧机构",
          "<b>传感子系统</b>：距离（超声波/激光/红外）、温度（DS18B20/MLX90614）、可选编码器",
          "<b>执行子系统</b>：直流电机 / 步进电机 / 舵机 + 电机驱动模块",
          "<b>控制子系统</b>：Arduino（UNO/Nano/Mega）主控，状态机 + 决策逻辑",
          "<b>电源子系统</b>：电池、稳压、隔离与过流保护"]:
    story.append(B(t))

# 三、学习路径
story.append(H1("三、关键学习路径（八阶段）"))

story.append(H2("阶段 1｜电子基础（约 1~2 周）"))
for t in ["欧姆定律、串并联、功率计算；认识电阻/电容/电感/二极管/三极管/MOSFET/继电器/光耦",
          "万用表测电压、电流、电阻；面包板搭接电路",
          "产出：能读懂基本电路图，能独立搭一个简单电路"]:
    story.append(B(t))

story.append(H2("阶段 2｜Arduino 入门（约 1~2 周）"))
for t in ["板卡选型（Uno 易上手 / Nano 体积小 / Mega 引脚多）、安装 Arduino IDE",
          "数字/模拟输入输出、PWM、串口打印、millis() 非阻塞延时、中断",
          "产出：LED、按键、电位器、蜂鸣器、直流电机的编程控制"]:
    story.append(B(t))

story.append(H2("阶段 3｜传感器应用（约 1~2 周）"))
for t in ["距离：HC-SR04（超声波）、VL53L0X/TOF（激光，精度高）、红外避障",
          "温度：DS18B20（单总线）、MLX90614（红外非接触测温）、NTC 热敏电阻",
          "协议：OneWire / I2C / SPI；数据滤波（中值滤波、滑动平均）与阈值判定",
          "产出：能稳定读取距离与温度，并触发“检测→判断”"]:
    story.append(B(t))

story.append(H2("阶段 4｜执行器与驱动（约 2~3 周）"))
for t in ["直流电机 + L298N/TB6612：PWM 调速、正反转（用于滚动爬行）",
          "步进电机 + A4988/DRV8825：精确定位进给（推荐用于切断进给）",
          "舵机：抱管夹持 / 锁紧",
          "编码器反馈、电流检测（用于切断过载保护）",
          "产出：电机按指令动作，可调速、可定位"]:
    story.append(B(t))

story.append(H2("阶段 5｜电源管理（约 1 周）"))
for t in ["做一张电压/电流预算表（电机堵转电流 + 传感器 + 主控合计）",
          "稳压：AMS1117 / LM2596 / 7805；锂电池与保护板、防反接、保险/自恢复保险丝",
          "电机浪涌抑制与续流二极管、光耦隔离",
          "产出：供电稳定，电机启动时不把主控拉垮"]:
    story.append(B(t))

story.append(H2("阶段 6｜电路设计与仿真（约 2~4 周，符合你的路线重点）"))
for t in ["仿真工具：Proteus（支持 Arduino 仿真）、Tinkercad（在线、易上手）、Wokwi（在线）",
          "用仿真验证：供电能力、引脚分配、逻辑正确性、元件选型",
          "原理图与 PCB：立创EDA / KiCad / EasyEDA → 打样",
          "产出：经过仿真验证的完整电路原理图与 PCB"]:
    story.append(B(t))

story.append(H2("阶段 7｜机械结构（约 2~4 周）"))
for t in ["环形抱管爬行：抱管锁紧（弹簧/螺纹/舵机）+ 摩擦滚轮/链轮驱动",
          "切断机构：切管器 / 圆盘锯 / 砂轮片，务必设计防护罩",
          "3D 建模：Fusion 360 / SolidWorks / FreeCAD / Onshape；3D 打印与装配",
          "产出：可装配、能沿管滚动并切断的机械样机"]:
    story.append(B(t))

story.append(H2("阶段 8｜控制逻辑与集成（约 2~3 周）"))
for t in ["状态机：待机 → 爬行 → 检测 → 判断 → 执行（切断/报警/返航）",
          "多传感器融合与决策阈值；PID 控制（爬行速度 / 切断进给力）",
          "看门狗、急停、异常处理；按模块逐级联调",
          "产出：整机完成“检测→判断→执行”无人化闭环"]:
    story.append(B(t))

# 四、决策点
story.append(H1("四、动手前必定的关键技术决策"))
for t in ["管道直径范围 → 决定抱管/滚轮结构尺寸",
          "切断方式（锯切 / 滚切 / 剪切）→ 决定执行器与动力",
          "供电方式（电池 / 有线）与续航要求",
          "是否需要无线通信（蓝牙 / ESP8266 / NRF24L01 / LoRa）与上位机",
          "检测项目与阈值 → 决定传感器选型"]:
    story.append(B(t))

# 五、资源
story.append(H1("五、推荐工具与资源"))
for t in ["Arduino 官方文档与库、B 站 / 慕课入门教程",
          "元器件数据手册（datasheet）查询（传感器/驱动模块官网）",
          "立创EDA / 嘉立创：画图 + 打样 + 元器件一站式",
          "仿真：Proteus / Tinkercad / Wokwi",
          "3D 打印平台与建模软件社区"]:
    story.append(B(t))

# 六、安全
story.append(H1("六、安全提醒"))
for t in ["高速旋转切断机构必须加防护罩，调试时远离身体与衣物",
          "电气安全：短路/过流保护、锂电池正确充电与存放",
          "无人化装置务必设计急停按钮与看门狗（防失控）"]:
    story.append(B(t))

# 七、时间表
story.append(H1("七、建议里程碑（业余时间约 3~6 个月）"))
data = [
    ["里程碑", "主要内容", "建议时长", "关键产出"],
    ["1. 电子+Arduino 基础", "电路与编程入门", "2~4 周", "可编程控制 LED/电机"],
    ["2. 传感检测", "距离/温度读取与判断", "2~3 周", "稳定读数 + 阈值触发"],
    ["3. 执行驱动", "电机/步进/舵机控制", "2~3 周", "可控速、可定位"],
    ["4. 电路仿真+PCB", "原理图仿真与打样", "3~5 周", "验证过的电路板"],
    ["5. 机械样机", "抱管爬行 + 切断机构", "3~6 周", "可装配机械样机"],
    ["6. 整机联调", "状态机 + 闭环控制", "2~4 周", "无人化闭环演示"],
]
tbl = Table(data, colWidths=[42*mm, 52*mm, 26*mm, 46*mm])
tbl.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "SimHei"),
    ("FONTNAME", (0, 1), (-1, -1), "Deng"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B8C4D0")),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(tbl)

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#B8C4D0"), spaceAfter=4))
story.append(P("提示：本路径为通用路线，具体顺序可根据已有基础调整；涉及高速旋转与切割，请始终把安全放在第一位。", st_note))

# ---------- 输出 ----------
OUT_DIR = r"E:\左面\claude交互文件"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PDF = os.path.join(OUT_DIR, "管道爬行切断装置_关键学习路径.pdf")

doc = SimpleDocTemplate(OUT_PDF, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=18*mm, bottomMargin=18*mm,
                        title="管道爬行切断装置 关键学习路径",
                        author="Claude Code")
doc.build(story)
print("PDF 已生成:", OUT_PDF)
