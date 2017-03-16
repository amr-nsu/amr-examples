#include "MDR32Fx.h"

#define DELAY 0x4FFFF
#define PIN1  0x0002

void gpio_init(void) {
    /* PORTA */
    MDR_RST_CLK->PER_CLOCK |= (1UL << 21); // Enable Clock

    /* PA1 */
    MDR_PORTA->OE     |= ((1 << 1));       // Output
    MDR_PORTA->ANALOG |= ((1 << 1));       // Digital
    MDR_PORTA->PWR    |= ((1 << 1*2));     // Low Speed Front
}

void gpio_toggle(uint16_t pin) {
    MDR_PORTA->RXTX ^= pin;
}

void delay(uint32_t delay) {
    volatile uint32_t i = delay;
    while(--i);
}

int main() {
    gpio_init();
    while(1) {
        gpio_toggle(PIN1);
        delay(DELAY);
    }
}


