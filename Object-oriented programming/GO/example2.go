package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
    // Перевірка наявності аргументів командного рядка
    if len(os.Args) < 2 {
        fmt.Println("Не вказано жодної команди для виконання.")
        return
    }

    // Отримання команди з аргументів командного рядка
    cmd := os.Args[1]
    args := os.Args[2:]

    // Виконання команди в системному шелі
    output, err := exec.Command(cmd, args...).Output()
    if err != nil {
        fmt.Println("Помилка виконання команди:", err)
        return
    }

    // Виведення результату в консоль
    fmt.Println(string(output))
}
