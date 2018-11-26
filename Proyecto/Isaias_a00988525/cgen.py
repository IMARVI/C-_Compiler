def codeGen(tree, file):
    f = open(file, "w+")
    code(tree, f)
    f.close()


def code(tree, f):
    if tree:
        # Init of the code
        if tree[0] == 'programa':
            f.write('.text\n')
            f.write('.align 2\n')
            f.write('.globl main\n')
            code(tree[1], f)
        elif tree[0] == 'expression':
            if len(tree) == 4:
                code(tree[3],f)
            else:
                code(tree[1],f)

        elif tree[0] == 'simple expression':
            # impoetante aqui se ahce una relop!!!!!!
            if len(tree) == 4:
                code(tree[1], f)
                code(tree[3], f)
                if tree[2][1] == '==':
                    f.write('   beq $a0 $t1 true1\n')
                elif tree[2][1] == '>':
                    f.write('   bgt $a0 $t1 true1\n')
                elif tree[2][1] == '<':
                    f.write('   blt $a0 $t1 true1\n')
                elif tree[2][1] == '>=':
                    f.write('   bge $a0 $t1 true1\n')
                elif tree[2][1] == '<=':
                    f.write('   ble $a0 $t1 true1\n')
                elif tree[2][1] == '!=':
                    f.write('   bne $a0 $t1 true1\n')
            else:
                code(tree[1], f)

        elif tree[0] == 'additive expression':
            # importante aqui se hacen los addop
            if len(tree) == 4:
                code(tree[1], f)
                f.write('   sw $a0 0($sp)\n')
                f.write('   addiu $sp $sp ‐4\n')
                code(tree[3], f)
                if tree[2][1] == '+':
                    f.write('   lw $t1 4($sp)\n')
                    f.write('   add $a0 $t1 $a0\n')
                    f.write('   addiu $sp $sp 4\n')
                else:
                    f.write('   lw $t1 4($sp)\n')
                    f.write('   sub $a0 $t1 $a0\n')
                    f.write('   addiu $sp $sp 4\n')
            else:
                code(tree[1], f)

        elif tree[0] == 'term':
            # importante aqui se hacen los mulop
            if len(tree) == 4:
                code(tree[1], f)
                f.write('   sw $a0 0($sp)\n')
                f.write('   addiu $sp $sp ‐4\n')
                code(tree[3], f)
                if tree[2][1] == '*':
                    f.write('   lw $t1 4($sp)\n')
                    f.write('   mult $a0 $t1 $a0\n')
                    f.write('   addiu $sp $sp 4\n')
                else:
                    f.write('   lw $t1 4($sp)\n')
                    f.write('   div $a0 $t1 $a0\n')
                    f.write('   addiu $sp $sp 4\n')
            else:
                code(tree[1], f)

        elif tree[0] == 'factor':
            if len(tree) == 4:
                code(tree[2], f)
            else:
                if type(tree[1]) == int:
                    x = tree[1]
                    f.write(f'  li $a0 {x}\n')
                else:
                    # se manda a llamar var,call
                    code(tree[1], f)

        elif tree[0] == 'statement':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'expression stmt':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'compound stmt':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'selection stmt':
            if len(tree) == 6:
                code(tree[3], f)
                f.write('   sw $a0 0($sp)\n')
                f.write('   addiu $sp $sp - 4\n')
                f.write('   lw $t1 4($sp)\n')
                f.write('   addiu $sp $sp 4\n')
                f.write('   beq $a0 $t1 true_branch\n')
                f.write('true_brach:\n')
                code(tree[5], f)
                f.write('b end_if:\n')
            elif len(tree) == 8:
                code(tree[3], f)
                f.write('   sw $a0 0($sp)\n')
                f.write('   addiu $sp $sp - 4\n')
                f.write('   lw $t1 4($sp)\n')
                f.write('   addiu $sp $sp 4\n')
                f.write('   beq $a0 $t1 true_branch\n')
                f.write('false_branch:\n')
                code(tree[7], f)
                f.write('   b end_if:\n')
                f.write('true_brach:\n')
                code(tree[5], f)
                f.write('   b end_if:\n')


        elif tree[0] == 'iteration stmt':
            f.write('while:\n')
            for x in range(1, len(tree)):
                code(tree[x], f)
            f.write('   j while\n')
            f.write('   exit:\n')

        elif tree[0] == 'return stmt':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'declaration list':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'fun declaration':
            # falta merer el nombre de la funcion
            f.write(f'{tree[2]}:\n')
            f.write('   move $fp $sp\n')
            f.write('   sw $ra 0($sp)\n')
            f.write('   addiu $sp $sp ‐4\n')
            for x in range(1, len(tree)):
                code(tree[x], f)
            f.write(f'     lw $ra 4($sp)\n')
            f.write(f'     addiu $sp $sp z\n')
            f.write(f'     lw $fp 0($sp)\n')
            f.write(f'     jr $ra\n')

        elif tree[0] == 'declaration':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'statement list':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'var declaration':
            if len(tree) == 7:
                f.write(f'  li $a0 {tree[2]}\n')
            else:
                for x in range(1, len(tree)):
                    code(tree[x], f)

        elif tree[0] == 'params':
            code(tree[1], f)

        elif tree[0] == 'param list':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'param':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'local declarations':
            for x in range(1, len(tree)):
                code(tree[x], f)

        elif tree[0] == 'var':
            if len(tree) == 5:
                code(tree[3], f)

        elif tree[0] == 'call':
            # falta checar si la funcion a llamar es input o autput
            if tree[0] == 'input':
                input()
            elif tree[0] == 'output':
                output()
            else:
                f.write('   sw $fp 0($sp)\n')
                f.write('   addiu $sp $sp ‐4\n')
                code(tree[3], f)
                f.write('   sw $a0 0($sp)\n')
                f.write('   addiu $sp $sp ‐4\n')
                f.write(f'  jal {tree[1]}\n')

        elif tree[0] == 'args':
            code(tree[1], f)

        elif tree[0] == 'args':
            code(tree[1], f)

        elif tree[0] == 'arg list':
            for x in range(1, len(tree)):
                code(tree[x], f)

compareKey = ['<', '>', ',>=', '<=', '==','!=']

def input():
    print('     li $v0, 5')
    print('     syscall')
    print('     move $t0, $v0')
    return

def output():
    print('     li $v0, 1')
    print('     move $a0, $t0')
    print('     syscall')
