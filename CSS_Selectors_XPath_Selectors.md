**Preference Rule**  

ID -> name -> className -> Link/Partial( a tag) -> css Selector -> Xpath. 



**XPath:** This locator type uses an XPath expression to locate an element on the page. (80%)

_**What is XPath?**_

XPath is a query language for selecting nodes from an HTML / XML document. XPath was defined by the World Wide Web Consortium.

1. **Absolute Xpath** -> `/html/body/div[2]//div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input`

2. **Relative XPath**  
   Core Logic: `//tagName[@attribute=value]`

Example:
```html
<input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
```
**XPath expressions:**
- `//input[@id="login-username"]`
- `//input[@name="username"]`
- `//input[@data-qa="hocewoqisi"]`

**Comparison:**
```xpath
//*[@name="username"] vs //input[@name="username"]
*   - Find all the elements -> which name --> username -> Slow
input -> Find all the input -> which name -> username  -> Fast
```
Example:
```html
<input type="text" name="firstname" value="" placeholder="First Name" id="input-firstname" class="form-control">

```xpath
- //input[@placeholder="First Name"]
- //input[@name="firstname"]
- //input[@id="input-firstname"]
```

**XPath Functions:**

### Known Attribute
- `//*[@id='btn-make-appointment']`

### TAG Name
- `//a[@id='btn-make-appointment']`

### Text Matching

1. **Full Visible Text** -> `text()`  
   `//a[text()="Make Appointment"]` 

2. **Partial Text** -> `contains()`
    - `//a[contains(text(),"Make Appointment")]`
    - `//a[contains(text(),'Make')]`
    - `//a[contains(text(),'Appointment')]`
    - `//a[contains(text(),'App')]`
    - `//a[contains(@id,'btn-make-appointment')]` 

3. **Starts-With**  
   //a[starts-with(text(),'Make')]

**Functions**

- **Contains()**  
  `//tag_name[contains(@attribute,'value_of_attribute')]`

- **Starts-with()**  
  `//tag_name[starts-with(@attribute,'Part_of_Attribute_value')]`

**Text()**  

```
  //tag_name[text()='Text of the element']
```

- **normalize-space()**  
  ```
  //a[normalize-space()="Make Appointment"]
  ```

### Operators - AND & OR

- **And Example**
   ```
   //tag_name[@name = 'Name value' and @id = ‘ID value’]
   ```
   ```
   //a[text()="Make Appointment" and contains(@id,"btn-make-appointment")]
   ```

- **Or Example**
   `//input[@placeholder ='Full Name' or @type = 'text']`


