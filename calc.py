#from math import *
import inspect
import matplotlib.pyplot as plt
import tkinter as tk
import sympy as sp
import math as math

motors_list = [

    
    "ДПР-32Н1-01",
    "ДПР-42Н1-01",
    "ДПР-52Н1-01",
    "ДПР-62Н1-01",
    "ДПР-72Н1-02",
    "ДПР-72Н1-01",
    "ДВИ-111-02",
    "ДВИ-121-02",
    "ДВИ-211-02",
    "ДВИ-221-02",
    "ДВИ-311-02",
    "ДВИ-321-02",
    "МИГ-60Б",
    "МИГ-90Б",
    "МИГ-40ДТ",
    "МИГ-90ДТ",
    "МИГ-180ДТ",
    "МИГ-370ДТ"
]

motors_params_list = [
    {"P_DN" : 1.9, "N_H" : 9000,  "U_YAN" : 27, "I_YAN" : 0.14, "R_YA" : 37, "J_D" : 0.2 * 10 ** (-6), "m_DV" : 0.08, "lambda_KD": 5.2},
    {"P_DN" : 4.7, "N_H" : 9000,  "U_YAN" : 27, "I_YAN" : 0.29, "R_YA" : 13, "J_D" : 0.57 * 10 ** (-6), "m_DV" : 0.15, "lambda_KD": 7.2},
    {"P_DN" : 9.4, "N_H" : 9000,  "U_YAN" : 27, "I_YAN" : 0.53, "R_YA" : 3.6, "J_D" : 1.7 * 10 ** (-6), "m_DV" : 0.26, "lambda_KD": 14.1},
    {"P_DN" : 12.6, "N_H" : 9000,  "U_YAN" : 27, "I_YAN" : 1.0, "R_YA" : 2.1, "J_D" : 3.6 * 10 ** (-6), "m_DV" : 0.41, "lambda_KD": 12.8},
    {"P_DN" : 18.8, "N_H" : 4500,  "U_YAN" : 27, "I_YAN" : 1.0, "R_YA" : 2.9, "J_D" : 7.8 * 10 ** (-6), "m_DV" : 0.6, "lambda_KD": 9.3},
    {"P_DN" : 25.1, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 1.35, "R_YA" : 1.7, "J_D" : 7.8 * 10 ** (-6), "m_DV" : 0.6, "lambda_KD": 11.8},
    {"P_DN" : 40, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 2.6, "R_YA" : 3.8, "J_D" : 7 * 10 ** (-6), "m_DV" : 1.5, "lambda_KD": 2.7},
    {"P_DN" : 60, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 3.6, "R_YA" : 2.5, "J_D" : 12 * 10 ** (-6), "m_DV" : 1.7, "lambda_KD": 3.0},
    {"P_DN" : 120, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 7.4, "R_YA" : 1.3, "J_D" : 23 * 10 ** (-6), "m_DV" : 3.4, "lambda_KD": 2.8},
    {"P_DN" : 180, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 10.8, "R_YA" : 0.8, "J_D" : 32 * 10 ** (-6), "m_DV" : 3.9, "lambda_KD": 3.1},
    {"P_DN" : 250, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 14.2, "R_YA" : 0.6, "J_D" : 45 * 10 ** (-6), "m_DV" : 6.3, "lambda_KD": 3.2},
    {"P_DN" : 370, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 20.5, "R_YA" : 0.4, "J_D" : 66 * 10 ** (-6), "m_DV" : 7.0, "lambda_KD": 3.3},
    {"P_DN" : 60, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 3.0, "R_YA" : 1.5, "J_D" : 3.6 * 10 ** (-6), "m_DV" : 1.5, "lambda_KD": 6.0},
    {"P_DN" : 90, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 4.1, "R_YA" : 0.7, "J_D" : 7.9 * 10 ** (-6), "m_DV" : 2.0, "lambda_KD": 9.4},
    {"P_DN" : 40, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 2.73, "R_YA" : 2.2, "J_D" : 2.9 * 10 ** (-6), "m_DV" : 1.6, "lambda_KD": 4.5},
    {"P_DN" : 90, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 4.6, "R_YA" : 0.73, "J_D" : 11 * 10 ** (-6), "m_DV" : 3.5, "lambda_KD": 8.0},
    {"P_DN" : 180, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 9.2, "R_YA" : 0.33, "J_D" : 17 * 10 ** (-6), "m_DV" : 5.7, "lambda_KD": 8.9},
    {"P_DN" : 370, "N_H" : 6000,  "U_YAN" : 27, "I_YAN" : 17.0, "R_YA" : 0.12, "J_D" : 48 * 10 ** (-6), "m_DV" : 9.0, "lambda_KD": 13.2}
]

image_count = 0

templateHeader = r'''
\documentclass{article}
    \usepackage[cp1251]{inputenc}  %% 1
    \usepackage[T2A]{fontenc}      %% 2
    \usepackage[russian]{babel}    %% 3

    % General document formatting
    \usepackage[margin=0.7in]{geometry}
    \usepackage[parfill]{parskip}
    \usepackage{graphicx}
    \graphicspath{ {./pictures/} }
    \hyphenation{:- }
    % Related to math
    \usepackage{amsmath,amssymb,amsfonts,amsthm}

\begin{document}

'''

templateFooter = r'''
\end{document}'''


def printx(name):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(f"{[var_name for var_name, var_val in callers_local_vars if var_val is name][0]} =", round(name, 3))

designation_global = "плечо"

designations = ["кисть", "локоть", "плечо"]

values_list = ["Абрамов Д.И.", "1", "0.15", "0.5", "1.0", "0.75", "0.4", "1", "0.05", "0.75", "0.4", "2", "2" ,"2", "1.5", "1", "0.5", "1.8", "2.5", "3.0", "3.0", "4.5", 
               "6.0", "3.0", "600", "240", "4", "9.81", "0.05", "0.8"]

label_list = ["Имя: ", "Вариант: ", "l2 (l1): ", "l3 / l1: ", "m1: ", "m2 / m1: ", "m3 / m1: ", "m: ", "J1: ", "J2 / J1: ", "J3 / J1: ", "r1 / l1: ", "r2 / l2: ", "r3 / l3: ",
              "phi_m1 / pi: ", "phi_m2 / pi: ", "phi_m3 / pi: ", "phi_1shtr_plecho: ", "phi_1shtr_lokot: ", "phi_1shtr_kist: ", "phi_2shrt_plecho: ", "phi_2shrt_lokot: ",
            "phi_2shrt_kist: ", "delta: ", "t1: ", "t3: ", "n: ", "g: ", "tau_omega_d: ", "eta_ph: ", "Привод: "]


root = tk.Tk()

def on_closing():
    # Add any cleanup code here before closing the window
    root.destroy()
    
def get_designation(dsg):
    global designation_global
    designation_global = dsg

root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("ZAPEKANOCHKA 2.0")


# Create labels and textboxes
labels = []
text_boxes = []
for c in range(29):
    label = tk.Label(root, text=label_list[c])
    label.grid(row=c, column=0)
    labels.append(label)
    
    text_box = tk.Entry(root, width=20)
    text_box.insert(0, values_list[c])
    text_box.grid(row=c, column=1)
    text_boxes.append(text_box)

for c in range(1):
    
    label = tk.Label(root, text=label_list[30+c])
    label.grid(row=(30+c), column=0)
    labels.append(label)
    options = tk.StringVar()
    text_box = tk.OptionMenu(root, options, command=get_designation, *designations)
    #text_box.insert(0, values_list[29+c])
    text_box.grid(row=30+c, column=1)
    text_boxes.append(text_box)


def make_plot(substitution_dict, md_equ, ud_eq, pe_eq, i1, i2):
    
    i = sp.symbols("i")
    tempUDMO = 0
    tempMDMO = 0
    prevSub = 1

    Mdmo = []
    Udmo = []
    Pemo = []

    v1 = i1.subs(substitution_dict).evalf()
    v2 = i2.subs(substitution_dict).evalf()

    #print (f"Plotting from {v1} to {v2}")
    
    if (isinstance(v1, sp.Integer) or isinstance(v1, sp.Float)):
        pass
    else:
        return 0
    
    if (isinstance(v2, sp.Integer) or isinstance(v2, sp.Float)):
        pass
    else:
        return 0
    

    icount = int(v1)
    
    # Итеративный поиск i
    for iicount in range(int(v1), int(v2)):
        substitution_dict[i] = iicount
        tempUDMO = ud_eq.subs(substitution_dict).evalf()
        tempMDMO = md_equ.subs(substitution_dict).evalf()
        if (isinstance(tempUDMO, sp.Integer) or isinstance(tempUDMO, sp.Float) or isinstance(tempUDMO, float) or isinstance(tempUDMO, int)):
            pass
        else:
            return 0
        if (isinstance(tempMDMO, sp.Integer) or isinstance(tempMDMO, sp.Float) or isinstance(tempMDMO, float) or isinstance(tempMDMO, int)):
            pass
        else:
            return 0
        if (abs(tempMDMO - tempUDMO) < abs(prevSub) ):
            icount = iicount
        prevSub = tempMDMO - tempUDMO

        #print(f"prevSub: {prevSub} tempMDMO {tempMDMO} tempUDMO: {tempUDMO}")


    #print(f"i equals {icount}")

    # matplotlib
    if (int(round(v1)) < int(round(v2))):
        x = range(int(round(v1)), int(round(v2)))
    else:
        x = range(int(round(v2)), int(round(v1)))
    
    for count in x:
        substitution_dict[i] = count
        Mdmo.append(abs(md_equ.subs(substitution_dict)).evalf())
        Udmo.append(abs(ud_eq.subs(substitution_dict)).evalf())
        Pemo.append(abs(pe_eq.subs(substitution_dict)).evalf())
    
    plt.clf()

    plt.plot(x, Mdmo, label='Mdmo')
    plt.plot(x, Udmo, label='Udmo')
    plt.plot(x, Pemo, label='Pemo')

    # добавляем заголовок и метки на оси
    plt.title("Подбор передаточного коэффициента")
    plt.xlabel('i')
    plt.ylabel('y')

    # добавляем легенду
    plt.legend()

    # НЕ выводим график, сохраняем его
    # plt.show()
    global image_count
    image_count = image_count + 1
    plt.savefig(f"./pictures/latest_{image_count}.png")
    

    return icount

def write_eqs(latex_lines_list = [], eqs_to_solve = [], eqs_names = []):
    for i in range(len(eqs_to_solve)):
        latex_lines_list += [
        sp.latex(sp.symbols(eqs_names[i])) + " = " + sp.latex(eqs_to_solve[i])
        ]

def solve_eqs(substitution_dict = {}, latex_lines_list = [], eqs_to_solve = [], eqs_names = [], consts_list = [0 for i in range(30)], motor_consts_list = [0 for i in range(10)]):
    
    latex_lines_list.append(r"\\Решение: \\")

    # Сначала пишем решение без ответов    
    write_eqs(latex_lines_list, eqs_to_solve, eqs_names)

    latex_lines_list.append(r"\\ Ответ: \\")

    for i in range(len(eqs_to_solve)):
        if (isinstance(eqs_to_solve[i], int) or isinstance(eqs_to_solve[i], float)):
            numeric_value = eqs_to_solve[i]
        else:
            numeric_value = eqs_to_solve[i].subs(substitution_dict).evalf()
        
        if (isinstance(numeric_value, sp.Integer) or isinstance(numeric_value, sp.Float) or numeric_value == 0):
            latex_lines_list += [
                sp.latex(sp.symbols(eqs_names[i])) + " = " + "{:.3f}".format(float(numeric_value))
            ]
        else:
            print("Failed solving " + eqs_names[i] + ": " + str(type(numeric_value)))
            print(numeric_value)

# Функция проверки пригодности выбранного мотора. Доступные режимы парааметры designation: "кисть", "локоть", "плечо"
def try_motor(substitution_dict = {}, latex_lines=[], motor_name = "", motor_params = {}, designation = "кисть", check_temp = 1):
    latex_lines_list = []
    lambda_KD,  P_DN,  N_H,  U_YAN, I_YAN, R_YA, J_D, m_DV = sp.symbols("lambda_KD  P_DN  N_H  U_YAN I_YAN R_YA J_D m_DV")
    # motors_params_list = [motor_params['P_DN'], motor_params['N_H'], motor_params['U_YAN'], motor_params['I_YAN'], motor_params['R_YA'], motor_params['J_D'], motor_params['m_DV']]
    # Определение символов
    l1, l2, l3, m1, m2, m3, m, J1, J2, J3, r1, r2, r3, phi_m1, phi_m2, phi_m3, phi_1shtr_plecho, phi_1shtr_lokot, phi_1shtr_kist, phi_2shrt_plecho,\
    phi_2shrt_lokot, phi_2shrt_kist, delta, t1, t3, n, g, tau_omega_d, eta_ph = sp.symbols('l1 l2 l3 m1 m2 m3 m J1 J2 J3 r1 r2 r3 phi_m1\
 phi_m2 phi_m3 phi_1шрт_плечо phi_1шрт_локоть phi_1шрт_кисть phi_2шрт_плечо\
 phi_2шрт_локоть phi_2шрт_кисть delta t1 t3 n g tau_omega_d eta_ph')

    # Определение символов для расчета двигла
    P_DN1, P_DN2, omega_DN, M_DN, K_M, K_OMEGA, R_UM, R_D, U_YAD, M_DD, M_DM, omega_DH, U_YA, t_omega_d, omega_e, P_M, M_P, P_max, i1, i2, m_pr, J_max,\
M_max, M_m_zvezda, M_TD, omega_TD, U_YAT, J_min, M_min, J_sr, M_sr, M_E_1, eta_oh, a_2shtr_R, a_2shtr_T, omega_D_max, a_1shtr_max, t_R,\
t_T, a_R, a_T, a_PS, t_PS, t_per, t2, M_E_2, a_2shtr, M_1shtr_DM, M_E_3, t_TS, M_E, m_p4, J_max, M_max, M_m, omega_ekv, i =\
sp.symbols('P_DN1 P_DN2 omega_DN M_DN K_M K_OMEGA R_UM R_D U_YAD M_DD M_DM omega_DH U_YA t_omega_d omega_e P_M M_P P_max i1 i2 m_pr J_max M_max M_m_zvezda\
 M_TD omega_TD U_YAT J_min M_min J_sr M_sr M_E_1 eta_oh a_2shtr_R a_2shtr_T omega_D_max a_1shtr_max t_R t_T a_R a_T a_PS t_PS t_per t2 M_E_2\
  a_2shtr M_1shtr_DM M_E_3 t_TS M_E m_p4 J_max M_max M_m omega_ekv i')

    # Определение универсальных символов для расчета трех видов
    phi_1shtr, phi_2shrt = sp.symbols("phi_1shtr phi_2shrt")
    M_max, J_min, M_min, phi_m = sp.symbols("M_max J_min M_min phi_m")
    
    substitution_dict.pop(i, None)

    if designation == "кисть":
        J_max = m3 * r3 * r3 + J3 + m * l3 * l3
        M_max = m3 * g * r3 + m * g * l3

        J_min = m3 * r3*r3 + J3
        M_min = m3 * g * r3

        phi_m = phi_m1
        phi_1shtr = phi_1shtr_kist
        phi_2shrt = phi_2shrt_kist

        M_m = J_max * phi_2shrt_kist + M_max
        omega_ekv = tau_omega_d * phi_2shrt_kist + phi_1shtr_kist
        P_M = (omega_ekv * M_m) / eta_ph
    elif designation == "локоть":
        m_pr = 3 * 2.5 * m_DV
        J_max = m2 * r2 * r2 + J2 + m_pr * l2 * l2 + m3 * ((l2 + r3) * (l2 + r3)) + J3 + m * ((l2 + l3) * (l2 + l3))
        M_max = m2 * g * r2 + m_pr * g * l2 + m3 * g * (l2 + r3) + m * g * (l2 + l3)

        J_min = J_max - m * ((l2 + l3) ** 2)
        M_min = M_max - m * g * (l2 + l3)
        
        phi_m = phi_m2
        phi_1shtr = phi_1shtr_lokot
        phi_2shrt = phi_2shrt_lokot
        
        M_m = J_max * phi_2shrt + M_max
        omega_ekv = tau_omega_d * phi_2shrt_lokot + phi_1shtr_lokot
        P_M = (omega_ekv * M_m) / eta_ph
    elif designation == "плечо":

        phi_m = phi_m3
        phi_1shtr = phi_1shtr_plecho
        phi_2shrt = phi_2shrt_plecho
        m_p4 = 2.5 * m_DV
        J_max = m1 * sp.Pow(r1,2) + J1 + m_p4 + sp.Pow(l1,2) + m2 * sp.Pow((l1 + r2),2) + J2 + (m)*sp.Pow((l1 + l2),2) + m3 * sp.Pow((l1 + l2 + r3), 2) + J3 + m*sp.Pow((l1+l2+l3), 2)
        M_max = m1 * g * r1 + m_p4 * g * l1 + m2 * g * (l1 + r2) + (m) * g * (l1 + l2) + m3 * g * (l1 + l2 + r3) + m * g * (l1 + l2 + l3)

        J_min = J_max - m * (l1 + l2 + l3)*(l1 + l2 + l3)
        M_min = M_max - m * g * (l1 + l2 + l3)
        
        M_m = J_max*phi_2shrt+M_max
        omega_ekv = tau_omega_d*phi_2shrt_plecho+phi_1shtr_plecho
        P_M = (omega_ekv * M_m) / eta_ph
        P_max = P_M
    else:
        print("Неправильно задано назначение расчета двигателя!")
        return 0


    lambda_T = sp.symbols("lambda_T")
    lambda_SK, lambda_M, lambda_MM, lambda_SKM = sp.symbols("lambda_SK lambda_M lambda_MM lambda_SKM") 

        # параметры двигателя
    substitution_dict[lambda_KD] = motor_params["lambda_KD"]
    substitution_dict[P_DN] = motor_params["P_DN"]
    substitution_dict[N_H] = motor_params["N_H"]
    substitution_dict[U_YAN] = motor_params["U_YAN"]
    substitution_dict[I_YAN] = motor_params["I_YAN"]
    substitution_dict[R_YA] = motor_params["R_YA"]
    substitution_dict[J_D] = motor_params["J_D"]
    substitution_dict[m_DV] = motor_params["m_DV"]
    # TODO сделать перебор лямбд в диапазонах
    substitution_dict[lambda_T] = 0.6 # всегда 0.6
    substitution_dict[lambda_SKM] =  1 # всегда 1
    substitution_dict[lambda_SK] =  0.8 # от 0.8 до 0.9
    substitution_dict[lambda_M] =  2 # от 1.5 до 2
    substitution_dict[lambda_MM] =  4 # всегда 4


    latex_lines_list += [r"\section*{Характеристики двигателя "+motor_name+"}"]
    latex_lines_list += [
        sp.latex("lambda_KD") + " = " +  "{:.3f}".format(motor_params["lambda_KD"]),
        sp.latex("P_DN") + " = " +  "{:.3f}".format(motor_params["P_DN"]),
        sp.latex("N_H") + " = " +  "{:.3f}".format(motor_params["N_H"]),
        sp.latex("U_YAN") + " = " +  "{:.3f}".format(motor_params["U_YAN"]),
        sp.latex("I_YAN") + " = " +  "{:.3f}".format(motor_params["I_YAN"]),
        sp.latex("R_YA") + " = " +  "{:.3f}".format(motor_params["R_YA"]),
        sp.latex("J_D") + " = " +  "{:.3f}".format(motor_params["J_D"]),
        sp.latex("m_DV") + " = " +  "{:.3f}".format(motor_params["m_DV"])
    ]



    P_max = P_M

    P_DN1 = P_max / 2.5
    P_DN2 = P_max / 1.5

    # выбрали двигатель X и его характеристики

    omega_DN = sp.pi * N_H / 30
    M_DN = P_DN / omega_DN
    K_M = M_DN / I_YAN
    K_OMEGA = (U_YAN - R_YA * I_YAN) / omega_DN

    # Выбор УМ
    R_UM = 0

    R_D = R_YA * 1
    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [P_max, P_DN1, P_DN2, omega_DN, M_DN, K_M, K_OMEGA, R_UM, R_D], 
              eqs_names=["P_max","P_DN1","P_DN2","omega_DN","M_DN","K_M","K_OMEGA","R_UM","R_D"], consts_list=values_list)


    latex_lines_list += [r"\section*{Передаточные отношения}"]

    U_YAD = lambda_SK * U_YAN
    M_DD = lambda_M * M_DN
    M_DM = lambda_MM * M_DN

    omega_DH = U_YAD / K_OMEGA
    U_YA = U_YAD
    t_omega_d = R_D * J_D / (K_M * K_OMEGA)
    omega_e = t_omega_d * phi_2shrt + phi_1shtr
    P_M = omega_e * M_m / 0.8
    M_P = U_YA * K_M / R_D
    P_max = 0.25 * M_P * omega_DH
    
    # 09.12.2023 - окей, тут два квадратных уравнения. Сейчас поправим

    i1_U, i2_U = sp.symbols("i1_U i2_U")

    i1_U = (0.5 * omega_DH / omega_e) * (
                1 - sp.sqrt(1 - ((4 * omega_e * R_D * M_m) / (0.8 * K_M * K_OMEGA * omega_DH * omega_DH))))
    i2_U = (0.5 * omega_DH / omega_e) * (
                1 + sp.sqrt(1 - ((4 * omega_e * R_D * M_m) / (0.8 * K_M * K_OMEGA * omega_DH * omega_DH))))
    

    latex_lines_list += [r"Границы графика по напряжению:"]
    write_eqs(latex_lines_list=latex_lines_list, eqs_to_solve=[i1_U, i2_U], eqs_names=["i1", "i2"])

    i1i2M = sp.solve(((((M_m / (i * 0.8)) + J_D * phi_2shrt * i) / M_DD) - 1).subs(substitution_dict).evalf(), i)
    #print(i1i2M)
    #print(((((M_m / (i * 0.8)) + J_D * phi_2shrt * i) / M_DD) - 1).subs(substitution_dict).evalf())
    if (len(i1i2M) < 2):
        latex_lines_list += [r"Корней уравнения границ по моменту меньше 2."]
        #latex_lines += latex_lines_list
        print("Корней уравнения границ по моменту меньше 2.")
        return 0
    #i1_M_sol = i1_M.subs(substitution_dict).evalf()
    #i2_M_sol = i2_M.subs(substitution_dict).evalf()
    i1_U_sol = i1_U.subs(substitution_dict).evalf()
    i2_U_sol = i2_U.subs(substitution_dict).evalf()

    if (isinstance(i1i2M[0], (int, float, sp.Float, sp.Integer)) and isinstance(i1i2M[1], (int, float, sp.Float, sp.Integer)) and
        isinstance(i1_U_sol, (int, float, sp.Float, sp.Integer)) and isinstance(i2_U_sol, (int, float, sp.Float, sp.Integer))):
        pass
    else:
        latex_lines_list += [r"Уравнение передаточных коэффициентов не имеет действительных корней."]
        #latex_lines += latex_lines_list
        print("Уравнение передаточных коэффициентов не имеет действительных корней.")
        return 0

    i1_M_sol = min(i1i2M)
    i2_M_sol = max(i1i2M)

    if ((i2_U_sol < i1_M_sol) or (i2_M_sol < i1_U_sol)):
        latex_lines_list += [r"Диапазоны напряжения и мощности не имеют точек пересечения."]
        #latex_lines += latex_lines_list
        print("Диапазоны напряжения и мощности не имеют точек пересечения.")
        return 0

    #print (f"i1_M_sol: {i1_M_sol} i2_M_sol: {i2_M_sol} i1_U_sol: {i1_U_sol} i2_U_sol: {i2_U_sol}")

    if (i1_M_sol > i1_U_sol):
        i1 = i1_M_sol
    else:
        i1 = i1_U_sol
    
    if (i2_M_sol < i2_U_sol):
        i2 = i2_M_sol
    else:
        i2 = i2_U_sol

    #solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve=[i1, i2], eqs_names=["i1", "i2"], consts_list=values_list)
    
    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [U_YAD, M_DD, M_DM, omega_DH, U_YA, t_omega_d, omega_e, P_M, M_P, P_max], 
              eqs_names=["U_YAD","M_DD","M_DM","omega_DH","U_YA","t_omega_d","omega_e","P_M","M_P","P_max"], consts_list=values_list)

    latex_lines_list += [r"\section*{График параметров двигателя}"]
    
    md_equ = (((M_m / (i * 0.8)) + J_D * phi_2shrt * i) / M_DD)
    ud_eq = ((((M_m / (i * 0.8)) + J_D * phi_2shrt * i) * (R_YA / K_M) + K_OMEGA * i * phi_1shtr) / U_YAD)
    pe_eq = (((((M_m / (i * 0.8)) + J_D * phi_2shrt * i) * (R_YA / K_M) + K_OMEGA * i * phi_1shtr) * (
                (M_m / (i * 0.8)) + J_D * phi_2shrt * i) * (1 / K_M)) / (U_YAN * I_YAN))

    write_eqs(latex_lines_list, eqs_to_solve= [md_equ, ud_eq, pe_eq], 
              eqs_names=["md_equ", "ud_eq", "pe_eq"])
    
    latex_lines_list += [f"Чертим график с i1 = {int(i1)} и i2 = {int(i2)}"]

    substitution_dict[i] = make_plot(substitution_dict, md_equ, ud_eq, pe_eq, i1, i2) 
    if (substitution_dict[i] == 0):
        latex_lines_list += [r"Уравнение передаточных коэффициентов не имеет действительных корней."]
        #latex_lines += latex_lines_list
        print("Уравнение передаточных коэффициентов не имеет действительных корней.")
        return 0
    global image_count
    latex_lines_list += [r"\includegraphics{latest_"+str(image_count)+".png}"]


    M_m_zvezda = M_m / (i * eta_ph)
    M_TD = M_m_zvezda + J_D * i * phi_2shrt

    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [M_m_zvezda, M_TD], 
              eqs_names=["M_m_zvezda", "M_TD"], consts_list=values_list)

    latex_lines_list += [r"Проверяем условие: M_TD <= M_DD"]
    if (M_TD.subs(substitution_dict).evalf() <= M_DD.subs(substitution_dict).evalf()):
        pass
    else:
        latex_lines_list += [r"Двигатель не подходит по требуемому моменту."]
        #latex_lines += latex_lines_list
        print("Двигатель не подходит по требуемому моменту.")
        return 0
    latex_lines_list += [r"Условие по моменту соблюдается!"]

    omega_TD = i * phi_1shtr

    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [omega_TD], 
              eqs_names=["omega_TD"], consts_list=values_list)

    latex_lines_list += [r"Проверяем условие: omega_TD <= omega_DN"]
    if (omega_TD.subs(substitution_dict).evalf() <= omega_DN.subs(substitution_dict).evalf()):
        pass
    else:
        latex_lines_list += [r"Двигатель не подходит по скорости вращения вала."]
        #latex_lines += latex_lines_list 
        print("Двигатель не подходит по скорости вращения вала.")
        return 0
    latex_lines_list += [r"Условие по скорости вала соблюдается!"]

    U_YAT = ((R_YA * M_TD) / K_M) + K_OMEGA * omega_TD

    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [U_YAT], 
              eqs_names=["U_YAT"], consts_list=values_list)

    latex_lines_list += [r"Проверяем условие: U_YAT <= U_YAD"]
    if (U_YAT.subs(substitution_dict).evalf() <= U_YAD.subs(substitution_dict).evalf()):
        pass
    else:
        latex_lines_list += [r"Двигатель не подходит по напряжению."]
        #latex_lines += latex_lines_list
        print("Двигатель не подходит по напряжению.")
        return 0
    latex_lines_list += [r"Условие по напряжению соблюдается!"]

    if (check_temp):
        latex_lines_list += [r"\section*{Расчет двигателя на нагрев}"]


        J_sr = (J_min + J_max) * 0.5
        M_sr = (M_min + M_max) * 0.5

        solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [J_min, J_min, J_sr, M_sr], 
                eqs_names=["J_min", "J_min", "J_sr", "M_sr"], consts_list=values_list)

        latex_lines_list += [r"\section*{1 участок}"]

        M_E_1 = M_sr / (i * eta_ph * sp.sqrt(lambda_T))

        solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [M_E_1], 
                eqs_names=["M_E_1"], consts_list=values_list)

        latex_lines_list += [r"\section*{2 участок}"]

        eta_oh = eta_ph

        a_2shtr_R = (M_DM - (M_sr / (i * eta_ph))) / ((J_sr / (i * eta_ph)) + J_D * i)
        a_2shtr_T = (M_DM + (M_sr * eta_oh / (i))) / ((J_sr * eta_oh / (i)) + J_D * i)

        omega_D_max = (lambda_SKM * U_YAN / K_OMEGA) - R_D * M_sr / (K_OMEGA * K_M * i * eta_ph)
        a_1shtr_max = omega_D_max / i
        t_R = a_1shtr_max / a_2shtr_R
        t_T = a_1shtr_max / a_2shtr_T
        a_R = 0.5 * t_R * a_1shtr_max
        a_T = 0.5 * t_T * a_1shtr_max
        a_PS = phi_m2 - a_R - a_T
        t_PS = a_PS / a_1shtr_max
        t_per = t_R + t_T + t_PS
        t2 = n * t_per
        M_E_2 = sp.sqrt(((M_DM * M_DM * (t_R + t_T) + t_PS * (M_sr / (i * eta_ph)) ** 2) / (t_per * lambda_T)))
        
        solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [eta_oh, a_2shtr_R, a_2shtr_T, omega_D_max, a_1shtr_max, t_R, t_T,
                                                                                                            a_R, a_T, a_PS, t_PS, t_per, t2, M_E_2], 
                eqs_names=["eta_oh", "a_2shtr_R", "a_2shtr_T", "omega_D_max", "a_1shtr_max", "t_R", "t_T", "a_R", "a_T", "a_PS", "t_PS", "t_per", "t2", "M_E_2"], consts_list=values_list)

        latex_lines_list += [r"\section*{3 участок}"]
        a_2shtr = 0.6 * phi_2shrt
        M_1shtr_DM = ((J_sr / i) + J_D * i) * a_2shtr
        M_E_3 = sp.sqrt((0.5 * M_1shtr_DM * M_1shtr_DM + (M_sr / (i * eta_ph)) ** 2) / lambda_T)

        solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [a_2shtr, M_1shtr_DM, M_E_3], 
                eqs_names=["a_2shtr", "M_1shtr_DM", "M_E_3"], consts_list=values_list)

        latex_lines_list += [r"\section*{Результат расчета на нагрев}"]
        t_TS = t1 + t2 + t3
        M_E = sp.sqrt((M_E_1*M_E_1*t1+M_E_2*M_E_2*t2+M_E_3*M_E_3*t3)/(t_TS))

        solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_lines_list, eqs_to_solve= [t_TS, M_E], 
                eqs_names=["t_TS", "M_E"], consts_list=values_list)

        latex_lines_list += [r"Проверяем условие: M_DN >= M_E"]
        if (M_DN.subs(substitution_dict).evalf() >= M_E.subs(substitution_dict).evalf()):
            pass
        else:
            latex_lines_list += [r"Двигатель не подходит по условию на нагрев."]
            #latex_lines += latex_lines_list
            print("Двигатель не подходит по условию на нагрев.")
            return 0
        latex_lines_list += [r"Условие по нагреву соблюдается!"]
    latex_lines += latex_lines_list
    return m_DV.subs(substitution_dict).evalf()


def calculate():
    for i in range(29):
        values_list[i] = text_boxes[i].get()

   # Определение символов
    l1, l2, l3, m1, m2, m3, m, J1, J2, J3, r1, r2, r3, phi_m1, phi_m2, phi_m3, phi_1shtr_plecho, phi_1shtr_lokot, phi_1shtr_kist, phi_2shrt_plecho,\
    phi_2shrt_lokot, phi_2shrt_kist, delta, t1, t3, n, g, tau_omega_d, eta_ph = sp.symbols('l1 l2 l3 m1 m2 m3 m J1 J2 J3 r1 r2 r3 phi_m1\
 phi_m2 phi_m3 phi_1шрт_плечо phi_1шрт_локоть phi_1шрт_кисть phi_2шрт_плечо\
 phi_2шрт_локоть phi_2шрт_кисть delta t1 t3 n g tau_omega_d eta_ph')
    
    substitution_dict = {
        l1:  float(values_list[2]),
        l2:  float(values_list[2]),
        l3:  (float(values_list[2]) * float(values_list[3])),
        m1:  float(values_list[4]),
        m2:  (float(values_list[5]) * float(values_list[4])),
        m3:  (float(values_list[6]) * float(values_list[4])),
        m:  float(values_list[7]),
        J1:  float(values_list[8]),
        J2:  (float(values_list[9]) * float(values_list[8])),
        J3:  (float(values_list[10]) * float(values_list[8])),
        r1:  float(values_list[2]) / float(values_list[11]),
        r2:  float(values_list[2]) / float(values_list[12]),
        r3:  (float(values_list[2]) * float(values_list[3])) / float(values_list[13]),
        phi_m1:  float(values_list[14]) * sp.pi,
        phi_m2:  float(values_list[15])* sp.pi,
        phi_m3:  float(values_list[16]) * sp.pi,
        phi_1shtr_plecho:  float(values_list[17]),
        phi_1shtr_lokot:  float(values_list[18]),
        phi_1shtr_kist:  float(values_list[19]),
        phi_2shrt_plecho:  float(values_list[20]),
        phi_2shrt_lokot:  float(values_list[21]),
        phi_2shrt_kist:  float(values_list[22]),
        delta:  float(values_list[23]),
        t1:  float(values_list[24]),
        t3:  float(values_list[25]),
        n:  float(values_list[26]),
        g:  float(values_list[27]),
        tau_omega_d: float(values_list[28]),
        eta_ph: float(values_list[29]),  # кпд редуктора прямого хода
        sp.pi: math.pi,
        sp.I: 0
    }

    latex_code = []
    latex_code += [r"\section*{Условие задачи}"]

    latex_code += [
        sp.latex("l1") + " = " +  "{:.3f}".format(float(values_list[2])),
        sp.latex("l2") + " = " +  "{:.3f}".format(float(values_list[2])),
        sp.latex("l3") + " = " +  "{:.3f}".format((float(values_list[2]) * float(values_list[3]))),
        sp.latex("m1") + " = " +  "{:.3f}".format(float(values_list[4])),
        sp.latex("m2") + " = " +  "{:.3f}".format((float(values_list[5]) * float(values_list[4]))),
        sp.latex("m3") + " = " +  "{:.3f}".format((float(values_list[6]) * float(values_list[4]))),
        sp.latex("m") + " = " +  "{:.3f}".format(float(values_list[7])),
        sp.latex("J1") + " = " +  "{:.3f}".format(float(values_list[8])),
        sp.latex("J2") + " = " +  "{:.3f}".format((float(values_list[9]) * float(values_list[8]))),
        sp.latex("J3") + " = " +  "{:.3f}".format((float(values_list[10]) * float(values_list[8]))),
        sp.latex("r1") + " = " +  "{:.3f}".format(float(values_list[2]) / float(values_list[11])),
        sp.latex("r2") + " = " +  "{:.3f}".format(float(values_list[2]) / float(values_list[12])),
        sp.latex("r3") + " = " +  "{:.3f}".format((float(values_list[2]) * float(values_list[3])) / float(values_list[13])),
        sp.latex("phi_m1") + " = " +  "{:.3f}".format(float(values_list[14]) * sp.pi),
        sp.latex("phi_m2") + " = " +   "{:.3f}".format(float(values_list[15])* sp.pi),
        sp.latex("phi_m3") + " = " +   "{:.3f}".format(float(values_list[16]) * sp.pi),
        sp.latex("phi_1shtr_plecho") + " = " +   "{:.3f}".format(float(values_list[17])),
        sp.latex("phi_1shtr_lokot") + " = " +   "{:.3f}".format(float(values_list[18])),
        sp.latex("phi_1shtr_kist") + " = " +   "{:.3f}".format(float(values_list[19])),
        sp.latex("phi_2shrt_plecho") + " = " +   "{:.3f}".format(float(values_list[20])),
        sp.latex("phi_2shrt_lokot") + " = " +   "{:.3f}".format(float(values_list[21])),
        sp.latex("phi_2shrt_kist") + " = " +   "{:.3f}".format(float(values_list[22])),
        sp.latex("delta") + " = " +   "{:.3f}".format(float(values_list[23])),
        sp.latex("t1") + " = " +   "{:.3f}".format(float(values_list[24])),
        sp.latex("t3") + " = " +   "{:.3f}".format(float(values_list[25])),
        sp.latex("n") + " = " +   "{:.3f}".format(float(values_list[26])),
        sp.latex("g") + " = " +   "{:.3f}".format(float(values_list[27])),
        sp.latex("tau_omega_d") + " = " +  "{:.3f}".format(float(values_list[28])),
        sp.latex("eta_ph") + " = " +  "{:.3f}".format(float(values_list[29]))
    ]

    J_max, M_max, M_m, omega_ekv, P_M = sp.symbols('J_max M_max M_m, omega_ekv P_M')
    # приближенный расчёт кисти
    #
    J_max = m3 * r3 * r3 + J3 + m * l3 * l3
    M_max = m3 * g * r3 + m * g * l3
    M_m = J_max * phi_2shrt_kist + M_max
    omega_ekv = tau_omega_d * phi_2shrt_kist + phi_1shtr_kist
    P_M = (omega_ekv * M_m) / eta_ph


    # Генерация LaTeX кода для формул
    latex_code += [r"\section*{Расчет кисти}"]
    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_code, eqs_to_solve= [J_max, M_max, M_m, omega_ekv, P_M], 
              eqs_names=["J_max", "M_max", "M_m", "omega_ekv", "P_M"], consts_list=values_list)
    rc = 0
    ch_temp = 0
    global designation_global
    for n_motor in range(len(motors_list)):
        if (designation_global == "кисть"):
            ch_temp = 1
        else:
            ch_temp = 0
        rc = try_motor(latex_lines=latex_code, motor_name = motors_list[n_motor], motor_params = motors_params_list[n_motor],
                         substitution_dict=substitution_dict, designation = "кисть", check_temp=ch_temp) 
        if (rc):
            latex_code += [r"\section*{Двигатель " + motors_list[n_motor] + " подходит к условию}"]
            print("Двигатель " + motors_list[n_motor] + " подходит к условию")
            break
        else:
            pass
            #latex_code += [r"\section*{Двигатель не подходит к условию}"]

    if (rc == 0):
        latex_code += ["Расчет кисти завершен неудачно, ни один двигатель не подошел!"]
        print("Расчет кисти завершен неудачно, ни один двигатель не подошел!")
        writeFile(latex_code)
        return 0
    

    latex_code += [r"\section*{Расчет локтя}"]
    # полный расчёт локтя
    m_DV = sp.symbols("m_дв")
    substitution_dict[m_DV] = rc
    m_pr = 3 * 2.5 * m_DV
    J_max = m2 * r2 * r2 + J2 + m_pr * l2 * l2 + m3 * ((l2 + r3) * (l2 + r3)) + J3 + m * ((l2 + l3) * (l2 + l3))
    M_max = m2 * g * r2 + m_pr * g * l2 + m3 * g * (l2 + r3) + m * g * (l2 + l3)
    M_m = J_max * phi_2shrt_lokot + M_max

    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_code, eqs_to_solve= [m_pr, J_max, M_max, M_m], 
              eqs_names=["m_pr", "J_max", "M_max", "M_m"], consts_list=values_list)
    
    for n_motor in range(len(motors_list)):
        if (designation_global == "локоть"):
            ch_temp = 1
        else:
            ch_temp = 0
        rc = try_motor(latex_lines=latex_code, motor_name = motors_list[n_motor], motor_params = motors_params_list[n_motor],
                         substitution_dict=substitution_dict, designation = "локоть", check_temp=ch_temp) 
        if (rc):
            latex_code += [r"\section*{Двигатель " + motors_list[n_motor] + " подходит к условию}"]
            print("Двигатель " + motors_list[n_motor] + " подходит к условию")
            break
        else:
            pass
            #latex_code += [r"Двигатель не подходит к условию"]
    if (rc == 0):
        latex_code += ["Расчет локтя завершен неудачно, ни один двигатель не подошел!"]
        print("Расчет локтя завершен неудачно, ни один двигатель не подошел!")
        writeFile(latex_code)
        return 0

    latex_code += [r"\section*{Расчет плеча}"]

    substitution_dict[m_DV] = rc

    m_p4 = 2.5 * m_DV
    
    
    J_max = m1 * sp.Pow(r1,2) + J1 + m_p4 + sp.Pow(l1,2) + m2 * sp.Pow((l1 + r2),2) + J2 + m*sp.Pow((l1 + l2),2) + m3 * sp.Pow((l1 + l2 + r3), 2) + J3 + m*sp.Pow((l1+l2+l3), 2)
    M_max = m1 * g * r1 + m_p4 * g * l1 + m2 * g * (l1 + r2) + m * g * (l1 + l2) + m3 * g * (l1 + l2 + r3) + m * g * (l1 + l2 + l3)

    M_m = J_max*phi_2shrt_plecho+M_max
    omega_ekv = tau_omega_d*phi_2shrt_plecho+phi_1shtr_plecho
    P_M = (omega_ekv * M_m) / eta_ph

    P_max = P_M

    solve_eqs(substitution_dict=substitution_dict, latex_lines_list = latex_code, eqs_to_solve= [m_p4, J_max, M_max, M_m, omega_ekv, P_M, P_max], 
              eqs_names=["m_p4", "J_max", "M_max", "M_m", "omega_ekv", "P_M", "P_max"], consts_list=values_list)

    for n_motor in range(len(motors_list)):
        if (designation_global == "плечо"):
            ch_temp = 1
        else:
            ch_temp = 0
        rc = try_motor(latex_lines=latex_code, motor_name = motors_list[n_motor], motor_params = motors_params_list[n_motor],
                         substitution_dict=substitution_dict, designation = "плечо", check_temp=ch_temp) 
        if (rc):
            latex_code += [r"\section*{Двигатель " + motors_list[n_motor] + " подходит к условию}"]
            print("Двигатель " + motors_list[n_motor] + " подходит к условию")
            break
        else:
            pass
            #latex_code += [r"\section*{Двигатель не подходит к условию}"]
    if (rc == 0):
        latex_code += ["Расчет плеча завершен неудачно, ни один двигатель не подошел!"] 
        print("Расчет плеча завершен неудачно, ни один двигатель не подошел!")
        writeFile(latex_code)
        return 0
    
    writeFile(latex_code)


def writeFile(latex_code):
    maxLineLength = 3500
    # Запись LaTeX кода в файл
    with open('formulas.tex', 'w') as f:
        f.write(templateHeader)
        for i in latex_code:
            if len(i) < maxLineLength:
            #f.write(r"\newline")
                f.write(i + "\r\n")
            else:
                n = 0
                for n in range(len(i) // maxLineLength):
                    f.write(i[(maxLineLength*n):((maxLineLength+1)*n)] + r"\\" + "\r\n")
                f.write(i[((maxLineLength+1)*n):] + "\r\n")
        f.write(templateFooter)
    
    print("file written, converting to pdf!")
    # Компиляция LaTeX файла в PDF
    import os
    os.system('pdflatex formulas.tex -quiet')

    print("file converted, ready")
    root.destroy()

# Create button to read textboxes
read_button = tk.Button(root, text="Нажмите для начала расчета задачи (в среднем занимает 2-5 минут)", command=calculate)
read_button.grid(row=len(values_list)+1, columnspan=2)

root.mainloop()
