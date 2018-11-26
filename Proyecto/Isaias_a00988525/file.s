.text
.align 2
.globl main
minloc:
   move $fp $sp
   sw $ra 0($sp)
   addiu $sp $sp ‐4
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   add $a0 $t1 $a0
   addiu $sp $sp 4
  li $a0 1
while:
   blt $a0 $t1 true1
   blt $a0 $t1 true1
   sw $a0 0($sp)
   addiu $sp $sp - 4
   lw $t1 4($sp)
   addiu $sp $sp 4
   beq $a0 $t1 true_branch
true_brach:
b end_if:
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   add $a0 $t1 $a0
   addiu $sp $sp 4
   j while
   exit:
     lw $ra 4($sp)
     addiu $sp $sp z
     lw $fp 0($sp)
     jr $ra
sort:
   move $fp $sp
   sw $ra 0($sp)
   addiu $sp $sp ‐4
while:
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   sub $a0 $t1 $a0
   addiu $sp $sp 4
   blt $a0 $t1 true1
   sw $fp 0($sp)
   addiu $sp $sp ‐4
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  jal minloc
  li $a0 21
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   add $a0 $t1 $a0
   addiu $sp $sp 4
   j while
   exit:
     lw $ra 4($sp)
     addiu $sp $sp z
     lw $fp 0($sp)
     jr $ra
main:
   move $fp $sp
   sw $ra 0($sp)
   addiu $sp $sp ‐4
  li $a0 0
while:
  li $a0 10
   blt $a0 $t1 true1
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   add $a0 $t1 $a0
   addiu $sp $sp 4
   j while
   exit:
   sw $fp 0($sp)
   addiu $sp $sp ‐4
  li $a0 2
  li $a0 1
  li $a0 10
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  jal sort
  li $a0 0
while:
  li $a0 10
   blt $a0 $t1 true1
   sw $a0 0($sp)
   addiu $sp $sp ‐4
  li $a0 1
   lw $t1 4($sp)
   add $a0 $t1 $a0
   addiu $sp $sp 4
   j while
   exit:
     lw $ra 4($sp)
     addiu $sp $sp z
     lw $fp 0($sp)
     jr $ra
