// Math.h(C++).cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <math.h>
using namespace std;
void menu();
void math(int name)throw(char);
typedef struct counotinmenu {
    string notice;
}counotinmenu;
int main()
{
    int cou = 0;
    menu();
    while (1) {
        try {
            cout << "请输入序号：";
            cin >> cou;
            break;
        }
        catch (exception) {
            cout << "输入异常，请重新输入！";
        }
    }
    math(cou);
    return 0;
}
void menu() {
    cout << "====================\n";
    cout << "欢迎来到math库运算器（C++版）\n";
    cout << "现有如下功能可用，请记住你所要的功能对应的序号：\n";
    cout << "1、取大于等于x的最小的整数值          2、求x的正切值\n";
    cout << "3、求x的平方根                        4、求x的正弦值\n";
    cout << "5、求x的y次方                         6、求x的小数部分及整数部分\n";
    cout << "7、求x以e为底的对数                   8、返回x*(2**exp)\n";
    cout << "9、求(x的平方+y的平方)的值            10、求x/y的余数\n";
    cout << "11、求小于等于x的最大的整数值         12、求自然常数e的x次方\n";
    cout << "13、对x进行开方                       14、求x的绝对值\n";
    cout << "====================\n";
}
void math(int name) throw(char) {
    switch (name)
    {
        case 1: {
            double b;
            cout << "请输入数据：";
            cin >> b;
            cout << "结果是：" << ceil(b);
            break;
        }

        default:{
            try { throw(counotinmenu); }
            catch (counotinmenu) { cout << "序号不在菜单内！"; }
            break;
        }
            
    }
}