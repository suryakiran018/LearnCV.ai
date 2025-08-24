# CSS Guide

**CSS** (Cascading Style Sheets), the language used to style and layout web pages by controlling the appearance of HTML elements. 

CSS is essential for creating visually appealing and responsive websites.
---

## 1. Introduction to CSS

### What is CSS?
CSS is a stylesheet language used to define the presentation of HTML documents, including colors, fonts, layouts, and responsiveness. 

It separates content (HTML) from design, improving maintainability and flexibility.

### Why Use CSS?
- **Separation of Concerns**: Keeps styling separate from structure.
- **Consistency**: Applies uniform styles across multiple pages.
- **Responsiveness**: Enables adaptive designs for various devices.

### Setting Up CSS
CSS can be applied in three ways:
1. **Internal CSS**: Inside a `<style>` tag in the HTML `<head>`.
   ```html
   <head>
       <style>
           h1 { color: blue; }
       </style>
   </head>
   ```
2. **External CSS**: In a separate `.css` file, linked via `<link>`:
   ```html
   <head>
       <link rel="stylesheet" href="styles.css">
   </head>
   ```
   ```css
   /* styles.css */
   h1 { color: blue; }
   ```
3. **Inline CSS**: Using the `style` attribute on an element (not recommended for maintainability).
   ```html
   <h1 style="color: blue;">Heading</h1>
   ```

---

## 2. CSS Basics

### Syntax
CSS consists of selectors and declarations:
```css
selector {
    property: value;
}
```
Example:
```css
p {
    color: navy;
    font-size: 16px;
}
```

### Selectors
- **Element Selector**: Targets HTML tags.
  ```css
  h1 { color: red; }
  ```
- **Class Selector**: Targets elements with a specific class.
  ```css
  .intro { font-weight: bold; }
  ```
  ```html
  <p class="intro">Introduction text</p>
  ```
- **ID Selector**: Targets a unique element.
  ```css
  #header { background-color: lightgray; }
  ```
  ```html
  <div id="header">Header</div>
  ```
- **Universal Selector**: Targets all elements.
  ```css
  * { margin: 0; }
  ```
- **Attribute Selector**: Targets elements with specific attributes.
  ```css
  input[type="text"] { border: 1px solid black; }
  ```

### Cascade and Specificity
CSS applies styles based on:
- **Specificity**: More specific selectors take precedence (ID > Class > Element).
- **Order**: Later rules override earlier ones.
- **`!important`**: Forces a rule to take precedence (use sparingly).
  ```css
  p { color: blue !important; }
  ```

---

## 3. Common CSS Properties

### 3.1. Text and Fonts
Control text appearance:
```css
p {
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    color: #333;
    text-decoration: underline;
}
```

### 3.2. Box Model
Every element is a box with properties:
- **Margin**: Space outside the border.
- **Border**: Surrounds the padding.
- **Padding**: Space inside the border.
- **Content**: The actual content.
```css
div {
    margin: 10px;
    border: 2px solid black;
    padding: 15px;
    width: 200px;
    height: 100px;
}
```

### 3.3. Colors and Backgrounds
Set colors and backgrounds:
```css
body {
    background-color: #f0f0f0;
    background-image: url('image.jpg');
    background-size: cover;
    color: rgb(0, 128, 0);
}
```

### 3.4. Display and Positioning
Control layout:
- **Display**: Defines how an element is rendered.
  ```css
  .inline { display: inline; }
  .block { display: block; }
  .none { display: none; }
  ```
- **Position**: Controls element placement.
  ```css
  .fixed { position: fixed; top: 10px; right: 10px; }
  .absolute { position: absolute; top: 20px; left: 20px; }
  .relative { position: relative; }
  ```

---

## 4. Layout Techniques

### 4.1. Flexbox
Create flexible layouts:
```css
.container {
    display: flex;
    justify-content: space-between; /* Align items horizontally */
    align-items: center; /* Align items vertically */
    gap: 10px;
}
```
```html
<div class="container">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

### 4.2. Grid
Create grid-based layouts:
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 10px;
}
```
```html
<div class="grid-container">
    <div>Cell 1</div>
    <div>Cell 2</div>
    <div>Cell 3</div>
</div>
```

### 4.3. Responsive Design
Use relative units and media queries:
```css
/* Relative units */
img {
    width: 100%;
    max-width: 500px;
}

/* Media query for screens smaller than 600px */
@media (max-width: 600px) {
    body {
        font-size: 14px;
    }
}
```

---

## 5. Advanced CSS Features

### 5.1. Transitions and Animations
Add smooth transitions:
```css
button {
    background-color: blue;
    transition: background-color 0.3s ease;
}
button:hover {
    background-color: green;
}
```

Create keyframe animations:
```css
@keyframes slide {
    0% { transform: translateX(0); }
    100% { transform: translateX(100px); }
}
.box {
    animation: slide 2s infinite;
}
```

### 5.2. Pseudo-Classes and Pseudo-Elements
- **Pseudo-Classes**: Style based on state.
  ```css
  a:hover { color: red; }
  input:focus { border-color: blue; }
  ```
- **Pseudo-Elements**: Style specific parts of an element.
  ```css
  p::first-line { font-weight: bold; }
  p::before { content: "★ "; }
  ```

### 5.3. CSS Variables
Define reusable values:
```css
:root {
    --primary-color: #007bff;
}
button {
    background-color: var(--primary-color);
}
```

### 5.4. Responsive Images
Use `object-fit` and `srcset`:
```html
<img src="image.jpg" srcset="image-2x.jpg 2x" alt="Responsive image">
```
```css
img {
    object-fit: cover;
    width: 100%;
    height: 200px;
}
```

---

## 6. CSS with Flask (Optional)
Integrate CSS with Flask for dynamic web apps:
1. Create a `static` folder with `styles.css`:
   ```css
   body {
       font-family: Arial, sans-serif;
       background-color: #f4f4f4;
   }
   ```
2. Link in a Flask template (`templates/index.html`):

{% raw %}
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
   ```
{% endraw %}

3. Flask app:
   ```python
   from flask import Flask, render_template
   app = Flask(__name__)
   @app.route('/')
   def home():
       return render_template('index.html')
   ```

---

## 7. Best Practices

- **Use External CSS**: Avoid inline styles for maintainability.
- **Minify CSS**: Reduce file size for faster loading.
- **Normalize CSS**: Use a reset/normalize stylesheet (e.g., [normalize.css](https://necolas.github.io/normalize.css/)).
- **Adopt BEM/SMACSS**: Use naming conventions like BEM (Block-Element-Modifier) for scalability.
  ```css
  .button--primary { background-color: blue; }
  ```
- **Test Responsiveness**: Use browser developer tools to simulate different devices.
- **Ensure Accessibility**: Use high-contrast colors and semantic HTML.

---

## 8. Troubleshooting & Tips

### Common Issues
- **Styles Not Applying**: Check selector specificity or file path:
  ```css
  /* Ensure correct path */
  <link rel="stylesheet" href="/static/styles.css">
  ```
- **Responsive Issues**: Verify media query syntax and viewport meta tag:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
- **Browser Compatibility**: Use vendor prefixes for experimental properties:
  ```css
  .box {
      -webkit-transform: rotate(45deg);
      transform: rotate(45deg);
  }
  ```

### Performance Tips
- **Combine Selectors**: Reduce redundancy:
  ```css
  h1, h2, h3 { font-family: Arial; }
  ```
- **Use Critical CSS**: Inline critical styles for faster initial rendering.
- **Leverage CSS Frameworks**: Use Bootstrap or Tailwind CSS for rapid development.

---

## 9. Resources & Further Learning

- **Official Documentation**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)
- **Tutorials**: [CSS-Tricks](https://css-tricks.com/), [W3Schools CSS](https://www.w3schools.com/css/)
- **Books**: "CSS: The Definitive Guide" by Eric Meyer and Estelle Weyl
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/css), [CSSWG GitHub](https://github.com/w3c/csswg-drafts)

---