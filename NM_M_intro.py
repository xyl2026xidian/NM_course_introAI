# numerical_methods_course_intro.py - 工程数值方法课程介绍
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

st.set_page_config(page_title="工程数值方法 · 课程介绍", layout="wide", page_icon="🚀")

# ========== 自定义样式 ==========
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .big-font {
        font-size: 28px !important;
        font-weight: bold;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    .emoji-big {
        font-size: 48px;
    }
    .highlight-blue {
        color: #1a73e8;
        font-weight: bold;
    }
    .highlight-red {
        color: #ea4335;
        font-weight: bold;
    }
    .highlight-green {
        color: #34a853;
        font-weight: bold;
    }
    .highlight-orange {
        color: #fbbc04;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


def set_chinese_font(fig):
    fig.update_layout(
        font=dict(family="SimHei, Microsoft YaHei, Arial Unicode MS, sans-serif")
    )
    return fig


# ========== 侧边栏 ==========
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/books.png", width=80)
    st.title("🚀 工程数值方法")
    st.markdown("**课程介绍**")
    st.markdown("---")

    view = st.radio(
        "选择浏览方式",
        ["🏠 课程总览",
         "📖 四大板块",
         "🎯 能力路径",
         "🌟 课程特色",
         "🚀 快速预览"]
    )

# ============================================================
# 1. 课程总览
# ============================================================
if view == "🏠 课程总览":
    st.title("🚀 工程数值方法")
    st.subheader("把数学变成可以计算的力量")

    st.markdown("---")

    # 欢迎动画
    col_anim, col_text = st.columns([1, 2])
    with col_anim:
        if st.button("🎬 点击探索", use_container_width=True):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            st.balloons()
            st.success("欢迎来到工程数值方法的世界！")

    with col_text:
        st.markdown("""
        **工程数值方法**是机械、土木、航空、能源等工科专业的核心基础课。
        它教会我们：当方程<b>求不出精确解</b>时，如何用<b>数值方法逼近答案</b>，
        把数学变成可以<b>计算</b>的力量。
        """)

    st.markdown("---")

    # 四大核心指标
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="emoji-big">📚</div>
            <div style="font-size:32px;font-weight:bold;color:#1a73e8;">4</div>
            <div>知识模块</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="emoji-big">📐</div>
            <div style="font-size:32px;font-weight:bold;color:#ea4335;">25+</div>
            <div>核心算法</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card">
            <div class="emoji-big">💡</div>
            <div style="font-size:32px;font-weight:bold;color:#fbbc04;">20+</div>
            <div>工程应用</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="card">
            <div class="emoji-big">∞</div>
            <div style="font-size:32px;font-weight:bold;color:#34a853;">∞</div>
            <div>无限可能</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 一句话概括
    st.markdown("""
    <div style="background:linear-gradient(135deg, #0f0c29, #302b63, #24243e);color:white;padding:30px;border-radius:15px;text-align:center;">
        <div style="font-size:24px;">
            🚀 从航空发动机到新能源汽车 · 从桥梁抗震到芯片散热<br>
            每一个工程奇迹的背后，都有 <b>工程数值方法</b> 在默默计算
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# 2. 四大板块
# ============================================================
elif view == "📖 四大板块":
    st.title("📖 四大知识板块")

    with st.expander("📐 板块一：误差与传播", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **核心内容**
            - 绝对误差与相对误差
            - 有效数字
            - 截断误差与舍入误差
            - 误差传播规律
            - 泰勒展开与误差估计

            **核心问题**
            🤔 算出来的结果可信吗？
            """)
        with col2:
            st.markdown("""
            **关键词**
            🔹 绝对误差 · 🔹 相对误差 · 🔹 有效数字
            🔹 截断误差 · 🔹 舍入误差 · 🔹 泰勒展开

            **工程意义**
            理解数值计算的精度与可靠性
            """)

    with st.expander("📈 板块二：插值与拟合", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **核心内容**
            - 拉格朗日插值
            - 牛顿插值（差商表）
            - 样条插值（C²连续）
            - 最小二乘拟合
            - 勒让德正交多项式拟合

            **核心问题**
            🤔 如何用有限的点描绘无限的曲线？
            """)
        with col2:
            st.markdown("""
            **关键词**
            🔹 拉格朗日 · 🔹 牛顿 · 🔹 样条插值
            🔹 最小二乘 · 🔹 勒让德正交 · 🔹 差商

            **工程应用**
            从离散数据点还原连续规律
            """)

    with st.expander("🔢 板块三：代数问题", expanded=True):
        tab1, tab2, tab3, tab4 = st.tabs(["线性方程组", "非线性方程", "非线性方程组", "特征值"])
        with tab1:
            st.markdown("""
            **核心方法**
            - LU分解 · Cholesky分解
            - QR分解 · SVD分解

            **特点**
            直接求解大规模线性方程组
            """)
        with tab2:
            st.markdown("""
            **核心方法**
            - 二分法（保证收敛）
            - 牛顿法（二阶收敛）
            - 割线法（避免求导）

            **特点**
            求解单变量非线性方程
            """)
        with tab3:
            st.markdown("""
            **核心方法**
            - 牛顿法（直接求解）
            - 拟牛顿BFGS（无需雅可比）

            **特点**
            求解多变量非线性方程组
            """)
        with tab4:
            st.markdown("""
            **核心方法**
            - 幂法 · 反幂法
            - 子空间迭代法
            - Krylov子空间法

            **特点**
            计算结构固有频率与振型
            """)

        st.markdown("""
        **核心问题**
        🤔 如何让计算机快速求解大规模方程组？
        """)

    with st.expander("📊 板块四：连续问题", expanded=True):
        tab1, tab2, tab3 = st.tabs(["数值积分与微分", "常微分方程", "偏微分方程"])
        with tab1:
            st.markdown("""
            **核心方法**
            - 复合辛普森（O(h⁴)精度）
            - 高斯积分（最高代数精度）
            - 差商求导（前向/中心差分）

            **特点**
            处理无法解析积分的函数
            """)
        with tab2:
            st.markdown("""
            **核心方法**
            - 欧拉法（显式一阶）
            - 四阶龙格-库塔（经典RK4）
            - Newmark法（结构动力学）
            - Newmark+牛顿（非线性）
            - 打靶法（边值问题）

            **特点**
            求解初值/边值问题
            """)
        with tab3:
            st.markdown("""
            **核心方法**
            - 有限差分法（工程常用）
            - 伽辽金法（有限元基础）

            **特点**
            处理热传导/波动等物理场
            """)

        st.markdown("""
        **核心问题**
        🤔 如何处理连续变化的物理世界？
        """)

# ============================================================
# 3. 能力路径
# ============================================================
elif view == "🎯 能力路径":
    st.title("🎯 学习路径 · 能力进阶")

    steps = [
        {"step": "第一步", "name": "理解可信度", "desc": "误差与传播", "emoji": "📐"},
        {"step": "第二步", "name": "从数据到函数", "desc": "插值与拟合", "emoji": "📈"},
        {"step": "第三步", "name": "求解大规模方程", "desc": "代数问题", "emoji": "🔢"},
        {"step": "第四步", "name": "处理连续世界", "desc": "连续问题", "emoji": "📊"},
    ]

    cols = st.columns(4)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div style="background:white;padding:15px;border-radius:15px;text-align:center;
                        box-shadow:0 4px 15px rgba(0,0,0,0.08);height:200px;
                        display:flex;flex-direction:column;justify-content:center;">
                <div style="font-size:36px;">{step['emoji']}</div>
                <div style="font-size:14px;color:#666;">{step['step']}</div>
                <div style="font-size:18px;font-weight:bold;color:#1a73e8;">{step['name']}</div>
                <div style="font-size:13px;color:#888;">{step['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📈 能力进阶示意图")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4],
        y=[20, 45, 70, 95],
        mode='lines+markers',
        name='能力成长曲线',
        line=dict(color='#1a73e8', width=4),
        marker=dict(size=20, color=['#34a853', '#fbbc04', '#ea4335', '#1a73e8'])
    ))
    fig.update_layout(
        title="从理论到工程应用的能力跃升",
        xaxis=dict(
            tickmode='array',
            tickvals=[1, 2, 3, 4],
            ticktext=['误差与传播', '插值与拟合', '代数问题', '连续问题']
        ),
        yaxis=dict(title="能力水平 (%)", range=[0, 100]),
        height=350,
        showlegend=False
    )
    fig = set_chinese_font(fig)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 4. 课程特色
# ============================================================
elif view == "🌟 课程特色":
    st.title("🌟 课程特色")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background:white;padding:25px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:40px;text-align:center;">🧠</div>
            <h4 style="text-align:center;">原理先行</h4>
            <p style="text-align:center;color:#666;">理解算法背后的设计逻辑与适用条件</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:white;padding:25px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);margin-top:15px;">
            <div style="font-size:40px;text-align:center;">🎨</div>
            <h4 style="text-align:center;">可视辅助</h4>
            <p style="text-align:center;color:#666;">应力云图、变形动画、3D交互式模拟</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:white;padding:25px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:40px;text-align:center;">📐</div>
            <h4 style="text-align:center;">手算为本</h4>
            <p style="text-align:center;color:#666;">手算推导 + 编程验证相结合</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:white;padding:25px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);margin-top:15px;">
            <div style="font-size:40px;text-align:center;">🏗️</div>
            <h4 style="text-align:center;">工程落地</h4>
            <p style="text-align:center;color:#666;">航空、能源、汽车、芯片等真实案例</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 💡 学习建议")
    tips = [
        "理解而不是背诵 —— 关注算法的思想与适用条件",
        "手算验证 —— 通过简单例子理解算法的执行过程",
        "编程实践 —— 将算法转化为可运行的代码",
        "善用可视化 —— 让抽象的计算变得直观可感",
        "联系工程 —— 在真实问题中锻炼判断力"
    ]
    for tip in tips:
        st.markdown(f"✅ {tip}")

# ============================================================
# 5. 快速预览
# ============================================================
elif view == "🚀 快速预览":
    st.title("🚀 课程快速预览")

    st.markdown("""
    <div style="background:linear-gradient(135deg, #0f0c29, #302b63, #24243e);color:white;padding:30px;border-radius:15px;text-align:center;">
        <div style="font-size:20px;">
            🚀 工程数值方法 · 一句话懂
        </div>
        <div style="font-size:28px;font-weight:bold;margin-top:10px;">
            把 <span style="color:#fbbc04;">数学</span> 变成
            <span style="color:#34a853;">可以计算</span> 的力量
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="background:white;padding:20px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:32px;text-align:center;">📐</div>
            <h4 style="text-align:center;">误差与传播</h4>
            <p style="text-align:center;font-size:14px;color:#666;">
                理解数值解的<br>可信度
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:white;padding:20px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:32px;text-align:center;">📈</div>
            <h4 style="text-align:center;">插值与拟合</h4>
            <p style="text-align:center;font-size:14px;color:#666;">
                从离散数据<br>还原连续函数
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background:white;padding:20px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:32px;text-align:center;">🔢</div>
            <h4 style="text-align:center;">代数问题</h4>
            <p style="text-align:center;font-size:14px;color:#666;">
                求解大规模<br>方程组与特征值
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background:white;padding:20px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.08);">
            <div style="font-size:32px;text-align:center;">📊</div>
            <h4 style="text-align:center;">连续问题</h4>
            <p style="text-align:center;font-size:14px;color:#666;">
                数值积分、ODE、<br>PDE的数值解法
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 工程应用快速预览
    st.markdown("### 🏗️ 学了能做什么？")

    apps = [
        ("✈️", "航空发动机", "涡轮叶片热-振动耦合分析"),
        ("🚗", "新能源汽车", "电池模组热膨胀与频率漂移"),
        ("🌉", "桥梁结构", "有限元法受力变形计算"),
        ("💻", "芯片散热", "温度场模拟与热应力分析"),
        ("🚀", "火箭发动机", "高温高压结构完整性分析"),
        ("🌊", "流体力学", "CFD计算与气动优化")
    ]

    cols = st.columns(3)
    for i, (icon, name, desc) in enumerate(apps):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:#f8f9fa;padding:12px;border-radius:10px;margin-bottom:10px;border-left:4px solid #1a73e8;">
                <div style="font-size:24px;">{icon}</div>
                <div style="font-weight:bold;font-size:14px;">{name}</div>
                <div style="font-size:12px;color:#666;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("🚀 工程数值方法 · 课程介绍 | 开启数值计算之旅")