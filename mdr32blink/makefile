TARGET=$(notdir $(CURDIR))
CC=arm-none-eabi-gcc
HEX=arm-none-eabi-objcopy
SIZE=arm-none-eabi-size
CPU=cortex-m3
MCU=MDR1986VE9x
CFLAGS=-mcpu=$(CPU) -mthumb -O2 -ffunction-sections -fdata-sections -Wall -Wextra -Wshadow -Wredundant-decls -Wno-missing-field-initializers -pipe

LIB=../../emdr1986x-std-per-lib

LD=$(LIB)/CMSIS/CM3/DeviceSupport/MDR32F9Qx/startup/gcc/MDR32F9Qx.ld

-include sources.mk

OBJ_C:=$(SRC:%.c=%.o)
OBJ:=$(OBJ_C:%.S=%.o)

INC=\
    -Iinc \
    -I$(LIB)/Config \
    -I$(LIB)/CMSIS/CM3/CoreSupport \
    -I$(LIB)/CMSIS/CM3/DeviceSupport/MDR32F9Qx/inc \
    -I$(LIB)/CMSIS/CM3/DeviceSupport/MDR32F9Qx/startup \
    -I$(LIB)/MDR32F9Qx_StdPeriph_Driver/inc \
    -I$(LIB)/MDR32F9Qx_StdPeriph_Driver/inc/USB_Library \

all: $(TARGET).hex

$(TARGET).hex: .elf
	$(HEX) -O ihex $(TARGET).elf $(TARGET).hex
	$(SIZE) --format=berkeley $(TARGET).elf
	@echo 'Finished building: $@'
	@echo ' '

.elf: $(OBJ)
	$(CC) ${CFLAGS} -T $(LD) --specs=nosys.specs -Wl,--gc-sections -ffreestanding -nostartfiles -Wl,-Map=$(TARGET).map $(OBJ) -o $(TARGET).elf

%.o: %.c
	$(CC) ${CFLAGS} -DUSE_$(MCU) -D__STARTUP_CLEAR_BSS -D__START=main ${INC} -c $< -o $@
%.o: %.S
	$(CC) ${CFLAGS} -DUSE_$(MCU) -D__STARTUP_CLEAR_BSS -D__START=main ${INC} -c $< -o $@

clean:
	$(RM) *.hex *.elf *.map $(OBJ)
	@echo ' '
