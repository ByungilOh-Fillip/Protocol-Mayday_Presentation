
import sys
import re

path = 'c:/workspace/Protocol-Mayday/Protocol-Mayday_Presentation/protocol_mayday_presentation_standalone.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. remove first SVG background from body::before
content = re.sub(
    r'url\("data:image/svg\+xml;base64,PHN2ZyB4bWxucz.*?no-repeat,',
    '',
    content,
    flags=re.DOTALL
)
content = content.replace('background-size: min(760px, 58vw) auto, 72px 72px, 72px 72px, auto;', 'background-size: 72px 72px, 72px 72px, auto;')

# 2. replace .slide:not(.hero)::before with display: none;
content = re.sub(
    r'\.slide:not\(\.hero\)::before\s*\{.*?\}',
    '.slide:not(.hero)::before {\n  display: none;\n}',
    content,
    flags=re.DOTALL
)

# 3. replace .title-composition::before with display: none;
content = re.sub(
    r'\.title-composition::before\s*\{.*?\}',
    '.title-composition::before {\n  display: none;\n}',
    content,
    flags=re.DOTALL
)

# 4. remove duplicated text in project-title
content = re.sub(
    r'<p class="lead">추락한 항공기 안에서 AI Companion LUMI의 안내를 받으며 생존 절차를 직접 수행하는 교육형 탈출 게임\.</p>\s*<div class="project-meta">\s*<p><b>과제분야</b> 언리얼엔진 기반 교육 콘텐츠 개발</p>\s*<p><b>개발대상</b> 항공기 비상 탈출 절차 체험형 콘텐츠</p>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# 5. replace C++ / Blueprint
content = content.replace('</svg><b>C++ / Blueprint</b></span>', '</svg><b>C++</b></span>')
content = content.replace('C++, Blueprint, UMG', 'C++, UMG')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')

