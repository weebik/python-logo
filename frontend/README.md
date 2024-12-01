<!-- ABOUT THE PROJECT -->
# Svelte Frontend

This folder contains a frontend for [`python-logo`][project-root] built using [Svelte][svelte-url]. Svelte is a modern JavaScript framework for creating user interfaces.

**If you want to use a web interface, you need to [build](#build-for-flask) the project before running `app.py`.** The application is then built as a static website with a JavaScript bundle.



<!-- GETTING STARTED -->
## Getting Started

To get a local copy built, follow these simple steps.

### Prerequisites

Make sure you have the following installed:

- **Node.js**: Version 18 or higher

### Installation

1. Install the project with dependencies:

   ```sh
   npm install
   ```



<!-- USAGE -->
## Usage

You can build the project for [Flask][flask-url] backend to serve or run it in development mode (with hot reload). The built frontend will be placed in the `../dist` directory, at the root of the project. That directory is served then by the backend, and the app should run without any errors.

### Build for Flask

1. Build the project:

   ```sh
   npm run build
   ```

### Development Mode

1. Run the development server:

   ```sh
   npm run dev
   ```



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[project-root]: /
[flask-url]: https://flask.palletsprojects.com/en/stable
[svelte-url]: https://svelte.dev
