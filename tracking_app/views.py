from django.shortcuts import render
import re
from .forms import TrackingForm


def extract_tracking_numbers(html_content, button_name):
    if button_name == 'UPS':
        tracking_numbers = re.findall(r'tracknum=([A-Za-z0-9]+)&', html_content)
        unique_tracking_numbers = list(set(tracking_numbers))
        return unique_tracking_numbers
    elif button_name == 'Fedex':
        # 在这里执行Fedex运单跟踪逻辑
        # 例如，从html_content中提取Fedex的运单号
        return []
    elif button_name == 'DHL':
        # 在这里执行DHL运单跟踪逻辑
        # 例如，从html_content中提取DHL的运单号
        return []


# 添加一个全局变量
last_tracking_numbers = []

def index(request):
    global last_tracking_numbers  # 声明你要使用全局变量
    trackform = TrackingForm()

    tracking_numbers = []  # 初始化空列表，用于存储追踪号码

    if request.method == 'POST':
        form = TrackingForm(request.POST)

        if form.is_valid():
            button_name = request.POST.get('button_name')
            html_content_1 = form.cleaned_data['html_content_1']
            html_content_2 = form.cleaned_data['html_content_2']
            html_content_3 = form.cleaned_data['html_content_3']
            html_content = html_content_1 + '<br>' + html_content_2 + '<br>' + html_content_3

            tracking_numbers = extract_tracking_numbers(html_content, button_name)
            last_tracking_numbers = tracking_numbers  # 更新全局变量的值

            if button_name == 'UPS':
                # 在这里执行UPS运单跟踪逻辑
                pass
            elif button_name == 'Fedex':
                # 在这里执行Fedex运单跟踪逻辑
                pass
            elif button_name == 'DHL':
                # 在这里执行DHL运单跟踪逻辑
                pass
    else:  # GET请求
        tracking_numbers = last_tracking_numbers  # 使用上一次的运单号渲染页面

    return render(request, 'index.html', {"trackform": trackform, "tracking_numbers": tracking_numbers})

