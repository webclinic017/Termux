// (c) 2017 Yami Odymel
// This code is licensed under MIT license.
package main

import (
	"fmt"
	"html"
	"strconv"
)

func main() {
	// Hexadecimal ranges from: http://apps.timwhitlock.info/emoji/tables/unicode
	emoji := [][]int{
		// Emoticons icons.
		{128513, 128591},
		// Dingbats.
		{9986, 10160},
		// Transport and map symbols.
		{128640, 128704},
	}

	for _, value := range emoji {
		for x := value[0]; x < value[1]; x++ {
			// Unescape the string (HTML Entity -> String).
			str := html.UnescapeString("&#" + strconv.Itoa(x) + ";")

			// Display the emoji.
			fmt.Println(str)
		}
	}
}
