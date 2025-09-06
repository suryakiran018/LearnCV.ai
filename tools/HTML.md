# HTML Guide

**HTML** (HyperText Markup Language), the standard language for creating and structuring content on the web. 

HTML is the backbone of web pages, defining their structure and content.

---

## 1. Introduction to HTML

### What is HTML?
HTML is a markup language used to create the structure of web pages. 

It consists of elements (tags) that define content such as headings, paragraphs, images, links, and forms.

### Why Use HTML?
- **Foundation of the Web**: Structures content for browsers to render.
- **Universal**: Supported by all web browsers.
- **Integrates with CSS and JavaScript**: Enables styling and interactivity.

### Setting Up
No installation is required for HTML. Write HTML in a text editor (e.g., VS Code, Notepad++) and save files with a `.html` extension. Open them in a web browser to view the result.

---

## 2. HTML Basics

### Basic HTML Structure
An HTML document follows a standard structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

- `<!DOCTYPE html>`: Declares the document as HTML5.
- `<html lang="en">`: Root element with language attribute.
- `<head>`: Contains metadata, title, and links to CSS/JavaScript.
- `<body>`: Contains visible content.

### Common Tags
- **Headings**: `<h1>` to `<h6>` for titles and subtitles.
  ```html
  <h1>Main Heading</h1>
  <h2>Subheading</h2>
  ```
- **Paragraphs**: `<p>` for text blocks.
  ```html
  <p>This is a paragraph of text.</p>
  ```
- **Links**: `<a>` for hyperlinks.
  ```html
  <a href="https://example.com">Visit Example</a>
  ```
- **Images**: `<img>` for embedding images.
  ```html
  <img src="image.jpg" alt="Description of image">
  ```

### Attributes
Tags can have attributes to provide additional information:
- `id`: Unique identifier for an element.
- `class`: Group elements for styling or scripting.
- `style`: Inline CSS styling.
  ```html
  <p id="intro" class="text" style="color: blue;">Styled text</p>
  ```

---

## 3. Structuring Content

### Semantic HTML
Use semantic tags to improve accessibility and SEO:
- `<header>`: Page or section header.
- `<nav>`: Navigation links.
- `<main>`: Primary content.
- `<article>`: Independent content.
- `<section>`: Thematic grouping.
- `<footer>`: Page or section footer.
```html
<header>
    <h1>My Website</h1>
    <nav>
        <a href="#home">Home</a> | <a href="#about">About</a>
    </nav>
</header>
<main>
    <article>
        <h2>Article Title</h2>
        <p>Content goes here.</p>
    </article>
</main>
<footer>
    <p>&copy; 2025 My Website</p>
</footer>
```

### Lists
- **Ordered List** (`<ol>`):
  ```html
  <ol>
      <li>First item</li>
      <li>Second item</li>
  </ol>
  ```
- **Unordered List** (`<ul>`):
  ```html
  <ul>
      <li>Item A</li>
      <li>Item B</li>
  </ul>
  ```

### Tables
Create tabular data:
```html
<table border="1">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>30</td>
        </tr>
    </tbody>
</table>
```

---

## 4. Forms and Interactivity

### Creating Forms
Forms collect user input:
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    <button type="submit">Submit</button>
</form>
```

Common input types:
- `text`, `email`, `password`, `number`, `checkbox`, `radio`, `file`.

### Form Attributes
- `required`: Ensures the field is filled.
- `placeholder`: Displays hint text.
- `value`: Sets default input value.
```html
<input type="text" placeholder="Enter your name" required>
```

---

## 5. Advanced HTML Features

### 5.1. Embedding Media
- **Images**:
  ```html
  <img src="photo.jpg" alt="Photo" width="200">
  ```
- **Video**:
  ```html
  <video controls>
      <source src="video.mp4" type="video/mp4">
      Your browser does not support the video tag.
  </video>
  ```
- **Audio**:
  ```html
  <audio controls>
      <source src="audio.mp3" type="audio/mpeg">
      Your browser does not support the audio tag.
  </audio>
  ```

### 5.2. Canvas
Create dynamic graphics with `<canvas>`:
```html
<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'blue';
    ctx.fillRect(50, 20, 100, 60);
</script>
```

### 5.3. Meta Tags and SEO
Optimize for search engines:
```html
<head>
    <meta name="description" content="My website description">
    <meta name="keywords" content="HTML, web development">
    <meta name="author" content="Your Name">
</head>
```

### 5.4. Accessibility (a11y)
Improve accessibility with ARIA and semantic HTML:
```html
<button aria-label="Close window">X</button>
<img src="image.jpg" alt="Descriptive text for screen readers">
```

---

## 6. Integrating with CSS and JavaScript
Link external CSS and JavaScript files:
```html
<head>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js"></script>
</head>
```

Example CSS (`styles.css`):
```css
h1 {
    color: navy;
    text-align: center;
}
```

Example JavaScript (`script.js`):
```javascript
document.querySelector('h1').addEventListener('click', () => {
    alert('Heading clicked!');
});
```

---

## 7. Best Practices

- **Use Semantic HTML**: Improves accessibility and SEO.
- **Validate Code**: Use tools like [W3C Validator](https://validator.w3.org/) to check for errors.
- **Minimize Inline Styles**: Use external CSS for maintainability.
- **Optimize Images**: Use compressed images and specify `width`/`height` to improve performance.
- **Ensure Responsiveness**: Use `<meta name="viewport">` for mobile-friendly designs.
- **Test Accessibility**: Use tools like [WAVE](https://wave.webaim.org/) to ensure inclusivity.

---

## 8. Troubleshooting & Tips

### Common Issues
- **Broken Links/Images**: Verify `src` or `href` paths are correct.
  ```html
  <img src="images/photo.jpg" alt="Photo"> <!-- Ensure path exists -->
  ```
- **Form Not Submitting**: Check `action` and `method` attributes.
- **Browser Compatibility**: Test in multiple browsers (Chrome, Firefox, Safari).

### Performance Tips
- **Use Relative Paths**: Avoid absolute URLs for local assets.
- **Lazy Load Images**:
  ```html
  <img src="image.jpg" loading="lazy" alt="Lazy-loaded image">
  ```
- **Minify HTML**: Remove unnecessary whitespace for faster loading.

---

## 9. Resources & Further Learning

- **Official Documentation**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **Tutorials**: [W3Schools HTML](https://www.w3schools.com/html/)
- **Books**: "HTML and CSS: Design and Build Websites" by Jon Duckett
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/html), [HTML5 GitHub](https://github.com/whatwg/html)

---