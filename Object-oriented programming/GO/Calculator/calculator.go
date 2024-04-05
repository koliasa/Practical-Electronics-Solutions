package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Простий калькулятор")
	for {
		fmt.Print("Вираз: ")
		scanner.Scan()
		input := scanner.Text()
		result, err := evaluate(input)
		if err != nil {
			fmt.Println("Помилка:", err)
		} else {
			fmt.Println("Результат:", result)
		}
	}
}

func evaluate(input string) (float64, error) {
	tokens := strings.Fields(input)
	if len(tokens) != 3 {
		return 0, fmt.Errorf("невірний формат виразу")
	}

	num1, err := strconv.ParseFloat(tokens[0], 64)
	if err != nil {
		return 0, fmt.Errorf("неправильне перше число")
	}

	num2, err := strconv.ParseFloat(tokens[2], 64)
	if err != nil {
		return 0, fmt.Errorf("неправильне друге число")
	}

	var result float64
	switch tokens[1] {
	case "+":
		result = num1 + num2
	case "-":
		result = num1 - num2
	case "*":
		result = num1 * num2
	case "/":
		if num2 == 0 {
			return 0, fmt.Errorf("ділення на нуль")
		}
		result = num1 / num2
	default:
		return 0, fmt.Errorf("невідома операція")
	}
	return result, nil
}