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
		result, err := evaluateExpression(input)
		if err != nil {
			fmt.Println("Помилка:", err)
		} else {
			fmt.Println("Результат:", result)
		}
	}
}

func evaluateExpression(input string) (float64, error) {
	expression := strings.ReplaceAll(input, " ", "") // Видаляємо всі пробіли
	expr := strings.Split(expression, "")
	if len(expr) == 0 {
		return 0, fmt.Errorf("вираз порожній")
	}
	tokens := parseTokens(expr)
	if len(tokens) == 0 {
		return 0, fmt.Errorf("невірний формат виразу")
	}
	return evaluate(tokens)
}

func parseTokens(expr []string) []string {
	var tokens []string
	var token string
	for _, char := range expr {
		if isOperator(char) {
			if token != "" {
				tokens = append(tokens, token)
				token = ""
			}
			tokens = append(tokens, char)
		} else {
			token += char
		}
	}
	if token != "" {
		tokens = append(tokens, token)
	}
	return tokens
}

func isOperator(char string) bool {
	return char == "+" || char == "-" || char == "*" || char == "/"
}

func evaluate(tokens []string) (float64, error) {
	stack := []string{}
	operators := map[string]int{"+": 1, "-": 1, "*": 2, "/": 2}
	var postfix []string

	for _, token := range tokens {
		if isOperator(token) {
			for len(stack) > 0 && operators[token] <= operators[stack[len(stack)-1]] {
				postfix = append(postfix, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, token)
		} else {
			postfix = append(postfix, token)
		}
	}

	for len(stack) > 0 {
		postfix = append(postfix, stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}

	resultStack := []float64{}
	for _, token := range postfix {
		if isOperator(token) {
			if len(resultStack) < 2 {
				return 0, fmt.Errorf("невірний формат виразу")
			}
			num2 := resultStack[len(resultStack)-1]
			num1 := resultStack[len(resultStack)-2]
			resultStack = resultStack[:len(resultStack)-2]
			result := calculate(num1, num2, token)
			resultStack = append(resultStack, result)
		} else {
			num, err := strconv.ParseFloat(token, 64)
			if err != nil {
				return 0, fmt.Errorf("неправильне число: %s", token)
			}
			resultStack = append(resultStack, num)
		}
	}

	if len(resultStack) != 1 {
		return 0, fmt.Errorf("невірний формат виразу")
	}

	return resultStack[0], nil
}

func calculate(num1, num2 float64, operator string) float64 {
	switch operator {
	case "+":
		return num1 + num2
	case "-":
		return num1 - num2
	case "*":
		return num1 * num2
	case "/":
		return num1 / num2
	default:
		return 0
	}
}