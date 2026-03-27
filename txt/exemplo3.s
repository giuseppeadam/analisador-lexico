.global _start
.text
_start:
    LDR R0, =const_0
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_1
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VADD.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_2
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_3
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VMUL.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_4
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VADD.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_5
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VDIV.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_6
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_7
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VDIV.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R0, S0
    VMOV S0, R0
    VCVT.F64.S32 D0, S0
    BL push_d0
    LDR R0, =const_8
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_9
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VCVT.S32.F64 S0, D0
    VMOV R0, S0
    VCVT.S32.F64 S1, D1
    VMOV R1, S1
    MOV R2, #0
loop_div_0:
    CMP R0, R1
    BLT fim_div_0
    SUB R0, R0, R1
    ADD R2, R2, #1
    B loop_div_0
fim_div_0:
    MUL R2, R2, R1
    SUB R0, R0, R2
    VMOV S0, R0
    VCVT.F64.S32 D0, S0
    BL push_d0
    LDR R0, =const_10
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_11
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VCVT.S32.F64 S2, D1
    VMOV R3, S2
    LDR R0, =const_12
    VLDR D2, [R0]
loop_pot_0:
    CMP R3, #0
    BLE fim_pot_0
    VMUL.F64 D2, D2, D0
    SUB R3, R3, #1
    B loop_pot_0
fim_pot_0:
    VMOV D0, D2
    BL push_d0
    LDR R0, =const_13
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    LDR R0, =var_V
    VSTR D0, [R0]
    BL pop_d0
    LDR R0, =var_VAR
    VSTR D0, [R0]
    LDR R0, =var_VAR
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_14
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VADD.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_15
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VSUB.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_16
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VCVT.S32.F64 S0, D0
    VMOV R0, S0
    LDR R1, =history_count
    LDR R1, [R1]
    SUB R0, R1, R0
    LDR R1, =results_history
    LSL R0, R0, #3
    ADD R1, R1, R0
    VLDR D0, [R1]
    BL push_d0
    LDR R0, =const_17
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VSUB.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_18
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_19
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VADD.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_20
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_21
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VMUL.F64 D0, D0, D1
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VDIV.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_22
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_23
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VMUL.F64 D0, D0, D1
    BL push_d0
    LDR R0, =const_24
    VLDR D0, [R0]
    BL push_d0
    LDR R0, =const_25
    VLDR D0, [R0]
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VMUL.F64 D0, D0, D1
    BL push_d0
    BL pop_d0
    VMOV D1, D0
    BL pop_d0
    VADD.F64 D0, D0, D1
    BL push_d0
    B .


push_d0:
    PUSH {R0, R1, R2, LR}
    LDR R0, =stack_data
    LDR R1, =stack_top
    LDR R2, [R1]
    LSL R2, R2, #3
    ADD R0, R0, R2
    VSTR D0, [R0]
    LDR R2, [R1]
    ADD R2, R2, #1
    STR R2, [R1]
    POP {R0, R1, R2, PC}

pop_d0:
    PUSH {R0, R1, R2, LR}
    LDR R1, =stack_top
    LDR R2, [R1]
    SUB R2, R2, #1
    STR R2, [R1]
    LDR R0, =stack_data
    LSL R2, R2, #3
    ADD R0, R0, R2
    VLDR D0, [R0]
    POP {R0, R1, R2, PC}

.data
const_0: .double 4.0
const_1: .double 5.0
const_2: .double 2.0
const_3: .double 3.0
const_4: .double 5.0
const_5: .double 2.0
const_6: .double 6.0
const_7: .double 2.0
const_8: .double 7.0
const_9: .double 3.0
const_10: .double 5.0
const_11: .double 3.0
const_12: .double 1.0
const_13: .double 10.0
const_14: .double 4.0
const_15: .double 1.0
const_16: .double 1
const_17: .double 3.0
const_18: .double 1.0
const_19: .double 2.0
const_20: .double 3.0
const_21: .double 4.0
const_22: .double 5.0
const_23: .double 2.0
const_24: .double 6.0
const_25: .double 3.0
var_V: .double 0.0
var_VAR: .double 0.0
stack_top: .word 0
stack_data: .space 256
results_history: .space 256
history_count: .word 0