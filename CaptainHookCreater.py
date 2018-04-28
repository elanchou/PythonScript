class_string = raw_input('Class Type: ')
function_string = raw_input('Function: ')
first_split_list = function_string.split(':')
return_type = ''
function_name_list = []
params_type_list = []
params_name_list = []

for index, substring in enumerate(first_split_list):
    if substring.startswith('-'):
        s = substring.split(')')
        function_name_list.append(s[1].replace(' ',''))
        return_type = (s[0].split('('))[-1]
    elif substring.startswith('('):
        param = ''
        if not substring.endswith(';'):
            s = substring.split(' ')
            func_name = s[-1]
            function_name_list.append(func_name.replace(' ',''))
            param = (substring.split(func_name))[0]
        else:
            param = substring.split(';')[0]

        sub = param.split(')')
        param_name = sub[-1].replace(' ','')
        param_type = (sub[0].split('('))[-1]
        params_name_list.append(param_name)
        params_type_list.append(param_type)


chmethod_substring = ''
chsuper_substring = ''
chclasshook_substring = ''

list_num = len(function_name_list)
if list_num == len(params_type_list) and list_num == len(params_name_list):
    chmethod_substring = 'CHOptimizedMethod(' + str(list_num) + ', ' + 'self, ' + return_type + ', ' + class_string
    chsuper_substring = 'CHSuper' + str(list_num) + '(' + class_string
    chclasshook_substring = 'CHClassHook' + str(list_num) + '(' + class_string
    for i in range(list_num):
        chmethod_substring += ', '
        chmethod_substring += function_name_list[i]
        chmethod_substring += ', '
        chmethod_substring += params_type_list[i]
        chmethod_substring += ', '
        chmethod_substring += params_name_list[i]

        chsuper_substring += ', '
        chsuper_substring += function_name_list[i]
        chsuper_substring += ', '
        chsuper_substring += params_name_list[i]

        chclasshook_substring += ', '
        chclasshook_substring += function_name_list[i]

    chmethod_substring += ')'
    chsuper_substring += ');'
    chclasshook_substring += ');'

    print chmethod_substring
    print '------------'
    print chsuper_substring
    print '------------'
    print  chclasshook_substring



