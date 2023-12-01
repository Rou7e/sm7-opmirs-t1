## Автоматическая среда синтеза мехатронных систем

Авторы - студенты СМ7 Абрамов Д., Труханов В.

Методика расчета взята из материалов кафедры СМ7 МГТУ им. Н.Э. Баумана

Программа использует введенные данные для генерации отчета по синтезу. В отчете приводится подробный расчет параметров кисти, локтя, и плеча манипулятора, а также производится подбор двигателя, подходящего к каждому из звеньев.

### Инструменты, использованные при разработке
ОС Windows 10
1) Python 3.9
    1) SymPy
    2) TKinter
    3) MatPlotLib
2) MiKTeX

### Проверки двигателей

Для каждого двигателя проводится:
1) Проверка на скорость вращения вала;
2) Проверка на напряжение;
3) Проверка на момент вала;
4) Проверка на тепловыделение на 3 участках;
   
### Используемые двигатели и их параметры

| Название | P_DN | N_H | U_YAN | I_YAN | R_YA | J_D | m_DV | lambda_KD |
|---|---|---|---|---|---|---|---|---|
|ДПР-32Н1-01|1.9| 9000| 27| 0.14| 37|0.2 * 10 ** (-6)| 0.08| 5.2|
|ДПР-42Н1-01|4.7| 9000| 27| 0.29| 13|0.57 * 10 ** (-6)| 0.15| 7.2|
|ДПР-52Н1-01|9.4| 9000| 27| 0.53| 3.6|1.7 * 10 ** (-6)| 0.26| 14.1|
|ДПР-62Н1-01|12.6| 9000| 27| 1.0| 2.1|3.6 * 10 ** (-6)| 0.41| 12.8|
|ДПР-72Н1-02|18.8| 4500| 27| 1.0| 2.9|7.8 * 10 ** (-6)| 0.6| 9.3|
|ДПР-72Н1-01|25.1| 6000| 27| 1.35| 1.7|7.8 * 10 ** (-6)| 0.6| 11.8|
|ДВИ-111-02|40| 6000| 27| 2.6| 3.8|7 * 10 ** (-6)| 1.5| 2.7|
|ДВИ-121-02|60| 6000| 27| 3.6| 2.5|12 * 10 ** (-6)| 1.7| 3.0|
|ДВИ-211-02|120| 6000| 27| 7.4| 1.3|23 * 10 ** (-6)| 3.4| 2.8|
|ДВИ-221-02|180| 6000| 27| 10.8| 0.8|32 * 10 ** (-6)| 3.9| 3.1|
|ДВИ-311-02|250| 6000| 27| 14.2| 0.6|45 * 10 ** (-6)| 6.3| 3.2|
|ДВИ-321-02|370| 6000| 27| 20.5| 0.4|66 * 10 ** (-6)| 7.0| 3.3|
|МИГ-60Б|60| 6000| 27| 3.0| 1.5|3.6 * 10 ** (-6)| 1.5| 6.0|
|МИГ-90Б|90| 6000| 27| 4.1| 0.7|7.9 * 10 ** (-6)| 2.0| 9.4|
|МИГ-40ДТ|40| 6000| 27| 2.73| 2.2|2.9 * 10 ** (-6)| 1.6| 4.5|
|МИГ-90ДТ|90| 6000| 27| 4.6| 0.73|11 * 10 ** (-6)| 3.5| 8.0|
|МИГ-180ДТ|180| 6000| 27| 9.2| 0.33|17 * 10 ** (-6)| 5.7| 8.9|
|МИГ-370ДТ|370| 6000| 27| 17.0| 0.12|48 * 10 ** (-6)| 9.0| 13.2 |