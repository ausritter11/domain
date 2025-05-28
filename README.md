# Domain Application

This project uses environment variables for configuration.

## Environment Variables

The following variables are expected to be set in your environment or in a `.env` file:

- `APOLLO_API_KEY` – API key for the Apollo service.
- `GOOGLE_API_KEY` – API key for Google services.

You can create a `.env` file in the project root to set these variables during development.  An example is provided in `.env.example`.

**Do not commit your actual `.env` file to version control.**  The `.gitignore` file already ignores it.

