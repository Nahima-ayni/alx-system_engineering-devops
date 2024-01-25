### Loops in Bash:

#### 1. **`for` Loop:**
   - Used to iterate over a sequence (numbers, list of items, etc.).
   - Syntax:
     ```bash
     for variable in {start..end..increment}; do
       # Commands to be executed
     done
     ```
   - Example:
     ```bash
     for i in {1..5}; do
       echo "Iteration $i"
     done
     ```

#### 2. **`while` Loop:**
   - Continues to execute a set of commands as long as a specified condition is true.
   - Syntax:
     ```bash
     while [ condition ]; do
       # Commands to be executed
     done
     ```
   - Example:
     ```bash
     count=1
     while [ $count -le 5 ]; do
       echo "Iteration $count"
       ((count++))
     done
     ```

#### 3. **`until` Loop:**
   - Similar to `while` loop, but continues until a specified condition becomes true.
   - Syntax:
     ```bash
     until [ condition ]; do
       # Commands to be executed
     done
     ```
   - Example:
     ```bash
     count=1
     until [ $count -gt 5 ]; do
       echo "Iteration $count"
       ((count++))
     done
     ```

### Conditions in Bash:

#### 1. **`if` Statement:**
   - Executes a set of commands if a specified condition is true.
   - Syntax:
     ```bash
     if [ condition ]; then
       # Commands to be executed if condition is true
     fi
     ```
   - Example:
     ```bash
     age=18
     if [ $age -ge 18 ]; then
       echo "You are eligible to vote."
     fi
     ```

#### 2. **`if-else` Statement:**
   - Executes one set of commands if a condition is true and another set if it's false.
   - Syntax:
     ```bash
     if [ condition ]; then
       # Commands to be executed if condition is true
     else
       # Commands to be executed if condition is false
     fi
     ```
   - Example:
     ```bash
     age=15
     if [ $age -ge 18 ]; then
       echo "You are eligible to vote."
     else
       echo "You are not eligible to vote yet."
     fi
     ```

#### 3. **`case` Statement:**
   - Provides a way to match multiple conditions against a value.
   - Syntax:
     ```bash
     case expression in
       pattern1)
         # Commands for pattern1
         ;;
       pattern2)
         # Commands for pattern2
         ;;
       *)
         # Default commands
         ;;
     esac
     ```
   - Example:
     ```bash
     fruit="apple"
     case $fruit in
       "apple")
         echo "It's an apple."
         ;;
       "banana")
         echo "It's a banana."
         ;;
       *)
         echo "It's neither an apple nor a banana."
         ;;
     esac
     ```

### Parsing in Bash:

#### 1. **Command-Line Arguments:**
   - Access arguments passed to a script.
   - Example:
     ```bash
     # script.sh
     echo "First argument: $1"
     echo "Second argument: $2"
     ```

     ```bash
     $ bash script.sh arg1 arg2
     # Output:
     # First argument: arg1
     # Second argument: arg2
     ```

#### 2. **Variable Substitution:**
   - Use variables within strings.
   - Example:
     ```bash
     name="Alice"
     greeting="Hello, $name!"
     echo $greeting
     ```

     ```bash
     # Output: Hello, Alice!
     ```

#### 3. **Command Substitution:**
   - Capture the output of a command and use it as part of another command.
   - Syntax:
     ```bash
     result=$(command)
     ```
   - Example:
     ```bash
     files=$(ls)
     echo "Files in the current directory: $files"
     ```

     ```bash
     # Output: Files in the current directory: file1 file2 file3
     ```

#### 4. **Read User Input:**
   - Get input from the user during script execution.
   - Example:
     ```bash
     echo "Enter your name:"
     read name
     echo "Hello, $name!"
     ```

     ```bash
     # Output:
     # Enter your name:
     # Alice
     # Hello, Alice!
     ```

This beginner guide covers the basics of loops, conditions, and parsing in Bash scripting.
