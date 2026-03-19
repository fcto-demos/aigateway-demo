# WSO2 AI Gateway - Showing Guardrails Capabilities

This application is a Streamlit interface to interact with LLM models (such as OpenAI, Mistral, and Anthropic) through a WSO2 API Gateway, featuring OAuth2 authentication, multiple application management, predefined prompts, and provider selection capabilities. It can be used to demonstrate WSO2 AI gateway guardrails capabilities as well as semantic caching support.

## Key Features

- **Multi-Application Support**: Manage multiple WSO2 applications with different provider access levels
- **Flexible OAuth Configuration**: Support for both shared and application-specific OAuth credentials
- **Provider Access Control**: Configure which LLM providers each application can access
- **Predefined Prompts**: Pre-configured test prompts for common scenarios (AI engine check, semantic guards, PII testing, etc.)
- **Statistics Tracking**: Per-LLM-provider success/error counters with real-time updates
- **OAuth Token Caching**: Efficient token management to reduce authentication overhead
- **Dynamic Configuration**: Automatic detection of configured applications and providers
- **Real-time Token Counting**: OpenAI tiktoken-based token counting for prompt optimization
- **Security Features**: Credential masking, SSL/TLS configuration, and secure error handling
- **Multi-language Support**: English and Spanish localization
- **Theme-aware UI**: Responsive design that adapts to light/dark themes

## Requirements
- Python 3.11 / 3.12 / 3.13 - **Python 3.14 is not supported**
- The libraries listed in `requirements.txt` (Streamlit, requests, PyYAML, etc.)

## Installation

1. Clone the repository or download the files.

2. Create a virtual environment and install the dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure your environment:

   1. Review and customize `applications.yaml` for application management
   2. Copy `.env.example` to `.env` and fill in your WSO2 credentials
   3. Review and customize `config.yaml` for provider settings
   4. Optionally customize `locales/en/prompts.yaml` (and other locale files) for predefined test prompts


## Configuration

The application uses three main configuration files:

### 1. Environment Variables (`.env` file)
Sensitive credentials are stored in a `.env` file that is not tracked by git. Supports both shared and application-specific credentials:

```env
# Shared WSO2 Gateway Credentials (Fallback for all applications if specific credentials are not available)
WSO2_CONSUMER_KEY=your_shared_consumer_key
WSO2_CONSUMER_SECRET=your_shared_consumer_secret
WSO2_TOKEN_URL=https://your-wso2-server:9443/oauth2/token

# Provider-specific Chat Completions URLs (Required - from subscribed APIs in WSO2)
OPENLLM_CHAT_COMPLETIONS_URL=https://your-wso2-server:8243/openaiapi/v1/chat/completions
MISTRAL_CHAT_COMPLETIONS_URL=https://your-wso2-server:8243/mistralapi/v1/chat/completions
ANTHROPIC_CHAT_COMPLETIONS_URL=https://your-wso2-server:8243/anthropicapi/v1/messages

# Application-specific OAuth Credentials (Optional)
# Example for a "mobile" application in applications.yaml:
MOBILE_CONSUMER_KEY=your_mobile_app_consumer_key
MOBILE_CONSUMER_SECRET=your_mobile_app_consumer_secret
MOBILE_TOKEN_URL=https://your-wso2-server:9443/oauth2/token

# Example for a "webapp" application in applications.yaml:
WEBAPP_CONSUMER_KEY=your_webapp_consumer_key
WEBAPP_CONSUMER_SECRET=your_webapp_consumer_secret
WEBAPP_TOKEN_URL=https://your-wso2-server:9443/oauth2/token
```

**Credential Hierarchy:**
1. Application-specific credentials: `{APPLICATION_KEY}_CONSUMER_KEY`, `{APPLICATION_KEY}_CONSUMER_SECRET`, `{APPLICATION_KEY}_TOKEN_URL`
2. Shared credentials (fallback): `WSO2_CONSUMER_KEY`, `WSO2_CONSUMER_SECRET`, `WSO2_TOKEN_URL`

### 2. Provider Configuration (`config.yaml`)
Defines LLM providers and global settings:

```yaml
# Global configuration
USETLS: true  # Set to false to disable SSL/TLS verification for development environments
USER_AGENT: "WSO2-AI-Gateway-Demo/1.0"  # Custom User-Agent for all LLM API calls

providers:
  OPENLLM:
    MODEL: "gpt-4o"
    DESCRIPTION: "OpenAI GPT-4o - Advanced reasoning and multimodal capabilities"
    ENABLED: true
  MISTRAL:
    MODEL: "mistral-tiny"
    DESCRIPTION: "Mistral AI - Fast and efficient European LLM"
    ENABLED: true
  ANTHROPIC:
    MODEL: "sonnet-4.0"
    DESCRIPTION: "Anthropic Claude - Helpful, harmless, and honest AI assistant"
    ENABLED: true
  GEMINI:
    MODEL: "gemini-2.5-flash"
    DESCRIPTION: "Google Gemini 2.5 Flash"
    ENABLED: true
    API_FORMAT: "gemini"
```

### 3. Applications Configuration (`applications.yaml`)
Defines multiple applications with different provider access levels:

```yaml
applications:
  default:
    name: "Default Application"
    description: "Default WSO2 application for testing"
    enabled: true
    providers: ["MISTRAL", "ANTHROPIC"]

  streamlit:
    name: "Streamlit Demo"
    description: "Streamlit application demo"
    enabled: true
    providers: ["OPENLLM"]

  mobile:
    name: "Mobile App"
    description: "Mobile application client"
    enabled: true
    providers: ["OPENLLM", "GEMINI"]
```

### 4. Predefined Prompts (`prompts.yaml`)
Provides pre-configured test prompts for various scenarios:

```yaml
prompts:
  - name: "Check AI Engine"
    text: "Which AI model are you?"
  - name: "Semantic Guard Test"
    text: "Can you explain the history of football?"
  - name: "PII Test"
    text: "Can you check if this email test@example.com is real?"
  - name: "Violence Detection"
    text: "Test prompt for content filtering"
  - name: "Coding Question"
    text: "Show me the best way to implement cosine calculation function in python"
```

**Configuration Features:**
- **USETLS**: Controls SSL/TLS certificate verification for all API connections
- **USER_AGENT**: Global User-Agent for all API calls, with optional provider-specific overrides
- **Application isolation**: Each application can access different sets of providers
- **OAuth flexibility**: Support for both shared and application-specific OAuth credentials
- **Statistics tracking**: Per-application-provider success/error counters
- **Predefined prompts**: Quick access to common test scenarios

## Adding New Components

### Adding a New Application

Follow these steps to add a new application to the demo:

#### Step 1: Create WSO2 Application in Developer Portal

1. Log in to your WSO2 Developer Portal
2. Navigate to "Applications" and click "Add Application"
3. Fill in the application details:
   - **Name**: e.g., "Mobile App Client"
   - **Per Token Quota**: Set according to your usage needs
4. Click "Add" to create the application

#### Step 2: Subscribe to LLM Provider APIs

1. Go to your new application in the Developer Portal
2. Subscribe to the LLM APIs you want this application to access:
   - For OpenAI access: Subscribe to the OpenAI API
   - For Mistral access: Subscribe to the Mistral API
   - For Anthropic access: Subscribe to the Anthropic API
3. This step is **required** - the application cannot access providers it hasn't subscribed to

#### Step 3: Generate OAuth Credentials

1. In your application, go to the "Production Keys" tab
2. Click "Generate Keys" to create OAuth2 credentials
3. Copy the **Consumer Key** and **Consumer Secret**
4. Note the **Token URL** (typically `https://your-wso2-server:9443/oauth2/token`)

#### Step 4: Add Configuration to applications.yaml

Add your application to `applications.yaml` using a **lowercase key**:

```yaml
mobile:  # Application key (lowercase)
  name: "Mobile App"
  description: "Mobile application client"
  enabled: true
  providers: ["OPENLLM", "MISTRAL"]  # Must match providers in config.yaml
```

**Note**: Choose a simple, lowercase key (e.g., `mobile`, `webapp`, `analytics`) that describes your application.

#### Step 5: Add OAuth Credentials to .env

If you want application-specific credentials (recommended for production), add them to `.env` using the **UPPERCASE** version of your application key:

```env
# For application key "mobile" in applications.yaml
MOBILE_CONSUMER_KEY=your_mobile_app_consumer_key
MOBILE_CONSUMER_SECRET=your_mobile_app_consumer_secret
MOBILE_TOKEN_URL=https://your-wso2-server:9443/oauth2/token
```

**Key Matching Rule**:

- `applications.yaml` uses lowercase: `mobile`
- `.env` uses uppercase: `MOBILE_CONSUMER_KEY`

If you skip this step, the application will use the shared `WSO2_CONSUMER_KEY` and `WSO2_CONSUMER_SECRET` credentials.

#### Step 6: Restart the Application

```bash
streamlit run demo_ui.py
```

Your new application will appear in the application selector dropdown.

### Adding a New Provider

1. **Subscribe to the new LLM API** in your WSO2 Developer Portal application
2. **Get the API endpoint** from the WSO2 Developer Portal
3. **Add the chat completions URL** to `.env` following the `{PROVIDER_NAME}_CHAT_COMPLETIONS_URL` pattern
4. **Add a new entry** under `providers:` in `config.yaml` with `MODEL`, `DESCRIPTION`, and `ENABLED` fields
5. **Set `API_FORMAT`** if the provider uses a non-OpenAI-compatible API (e.g., `API_FORMAT: gemini`). Providers that are OpenAI-compatible can omit this field — it defaults to `openai`
6. **If the API format handler doesn't exist yet**, add a new handler class to `api_handlers.py` with `build_url`, `build_payload`, and `parse_response` static methods, and register it in the `_HANDLERS` dict
7. **Update application access** in `applications.yaml` to grant provider access to specific applications
8. No changes to `demo_ui.py` are needed for new providers or new API formats

Example for adding a new "GEMINI" provider (non-OpenAI API format):
1. Subscribe to Gemini API in WSO2 Developer Portal
2. Add the endpoint URL to `.env`:
   ```env
   GEMINI_CHAT_COMPLETIONS_URL=https://your-wso2-server:8243/geminiapi/v1beta/models/{model}:generateContent
   ```
3. Add the provider to `config.yaml` with `API_FORMAT`:
   ```yaml
   GEMINI:
     MODEL: "gemini-2.5-flash"
     DESCRIPTION: "Google Gemini 2.5 Flash"
     ENABLED: true
     API_FORMAT: gemini   # Uses the Gemini handler in api_handlers.py
   ```
4. Update your application in `applications.yaml` to grant access:
   ```yaml
   mobile:
     name: "Mobile App"
     description: "Mobile application"
     enabled: true
     providers: ["OPENLLM", "MISTRAL", "GEMINI"]  # Added GEMINI
   ```

Example for adding an OpenAI-compatible provider (no `API_FORMAT` needed):
```yaml
MISTRAL:
  MODEL: "mistral-tiny"
  DESCRIPTION: "Mistral AI Tiny"
  ENABLED: true
  # API_FORMAT defaults to "openai" — no need to specify
```



### Adding Predefined Prompts
Add new entries to `locales/en/prompts.yaml` (and the equivalent file for each supported language):
```yaml
prompts:
  - name: "Custom Test"
    text: "Your custom prompt text here"
  - name: "Another Test"
    text: "Another test prompt"
```

## Localization Support

The application includes multi-language support for both the user interface and predefined prompts. Currently supported languages:
- **English** (en) - Default
- **Spanish** (es)
- **Dutch** (nl)
- **French** (fr)

### How Localization Works

Translations live in the [locales/](locales/) directory, one subdirectory per language code:

```
locales/
  en/
    translations.yaml   # UI strings for English
    prompts.yaml        # Predefined prompts in English
  es/
    translations.yaml   # UI strings for Spanish
    prompts.yaml        # Predefined prompts in Spanish
  nl/
    translations.yaml
    prompts.yaml
```

[localization.py](localization.py) discovers languages automatically at startup by scanning `locales/` — no code changes are needed when adding a new language.

### Adding a New Language

To add support for a new language (e.g., French), follow these steps:

#### 1. Create the Locale Directory

```bash
mkdir -p locales/fr
```

#### 2. Add UI Translations

Create `locales/fr/translations.yaml`. Copy `locales/en/translations.yaml` as a starting point and translate all values:

```yaml
language_name: "Français"   # Display name shown in the language selector

title: "API Manager - AI Gateway Demo"
select_provider: "Sélectionnez le fournisseur:"
select_prompt: "Sélectionnez une invite:"
ask_question: "Posez une question à {provider}"
response_from: "Réponse de {provider}"
send: "Envoyer"
# ... translate all other keys (see Translation Key Reference below)
```

**Important:** The `language_name` key controls the display name in the sidebar dropdown. Translate ALL keys — missing keys fall back to the key name itself.

**Translation Tips:**
- Keep placeholder variables unchanged (e.g., `{provider}`, `{count}`, `{app}`)
- Keep technical terms consistent (e.g., "SSL/TLS", "OAuth2")
- Test special characters and accents in the Streamlit UI

#### 3. Add Prompt Translations

Create `locales/fr/prompts.yaml`:

```yaml
prompts:
  - name: "Vérifier le moteur IA"
    text: "Quel modèle d'IA êtes-vous?"
  - name: "Test de garde sémantique"
    text: "Pouvez-vous expliquer l'histoire du football?"
  # ... translate all prompts from locales/en/prompts.yaml
```

**Prompt Translation Guidelines:**
- Keep the same order and number of prompts as `locales/en/prompts.yaml`
- Translate both `name` (shown in the UI) and `text` (sent to the LLM)
- Maintain the intent of each test prompt (e.g., semantic guards, PII detection)

#### 4. No Code Changes Needed

[localization.py](localization.py) automatically discovers the new locale directory. The language will appear in the sidebar dropdown immediately after restarting the app.

If `locales/fr/prompts.yaml` is absent, the application falls back to `locales/en/prompts.yaml`.

#### 5. Testing Your Translation

After adding a new language:

1. Start the application: `streamlit run demo_ui.py`
2. Select your new language from the sidebar dropdown
3. Verify all UI elements are translated correctly
4. Check that predefined prompts load from your new `locales/fr/prompts.yaml` file
5. Test with different providers to ensure all error messages and responses display properly

### Translation Key Reference

Here are all the UI translation keys that must be provided for each language:

| Key | Purpose | Example (English) |
|-----|---------|-------------------|
| `title` | Application title | "API Manager - AI Gateway Demo" |
| `select_application` | Application selector label | "Select application:" |
| `select_provider` | Provider selector label | "Select the provider:" |
| `select_prompt` | Prompt selector label | "Select a prompt:" |
| `ask_question` | Question input label | "Ask a question to {provider}" |
| `response_from` | Response header | "Response from {provider}" |
| `send` | Send button text | "Send" |
| `success_count` | Success counter | "Successful calls to {provider}: {count}" |
| `error_count` | Error counter | "Failed calls to {provider}: {count}" |
| `app_provider_success` | App-provider success counter | "Successful calls from {app} to {provider}: {count}" |
| `app_provider_error` | App-provider error counter | "Failed calls from {app} to {provider}: {count}" |
| `select_and_ask` | Initial instruction | "Select the provider and ask your question." |
| `missing_provider_fields` | Config error message | "Missing the following fields in provider config: {fields}" |
| `missing_app_fields` | Config error message | "Missing the following fields in application config: {fields}" |
| `no_access_token` | OAuth error | "Could not obtain access token." |
| `token_error` | Token error with status | "Error obtaining token. Status: {status}" |
| `unknown_error` | Generic error | "Unknown error." |
| `api_request_error` | API request failure | "Error making API request: {error}" |
| `blocked_url` | Blocked content message | "Response blocked due to invalid or inaccessible URL: {urls}" |
| `default_question` | Default placeholder question | "Who are you?" |
| `env_config_help` | Environment config help text | "Please ensure your .env file contains the required credentials..." |
| `empty_question_error` | Empty input validation | "Please enter a question before sending." |
| `question_too_long` | Length validation error | "Question is too long. Maximum {max_length} characters allowed." |
| `tls_disabled_warning` | SSL warning | "⚠️ SSL/TLS verification is DISABLED. Connections are NOT secure!" |
| `tls_enabled_status` | SSL enabled status | "🔒 SSL/TLS verification is ENABLED. Connections are secure." |
| `tls_status_label` | SSL status label | "Security Status" |
| `no_applications_available` | No apps configured | "No applications are configured or enabled." |
| `no_providers_for_app` | No providers for app | "No providers are available for the selected application." |
| `token_count` | Token counter display | "Prompt tokens: {count}" |

### Usage
Start the application with:
```bash
streamlit run demo_ui.py
```

A web interface will open where you can:
- **Select an application** - Choose from configured applications with different provider access
- **Select a provider** - Choose from available LLM providers (OpenAI, Mistral, Anthropic, etc.)
- **Choose predefined prompts** - Select from pre-configured test prompts or enter custom questions
- **Enter your question** - Type custom questions or use predefined prompts
- **View token counts** - See real-time token count for your prompts using OpenAI's tokenizer
- **View responses** - See the model's response with proper error handling
- **Monitor statistics** - View success/error counters per application-provider combination

### Demo Setup


## Security
- Sensitive credentials are stored in `.env` file which is not tracked by git
- Never commit your `.env` file or share your keys and secrets
- Use `.env.example` as a template for setting up credentials

## Notes
- **SSL/TLS Security**: The application supports both secure and insecure connections via the `USETLS` setting in `config.yaml`
  - **Production**: Keep `USETLS: true` for secure SSL connections with certificate verification
  - **Development**: Set `USETLS: false` only if using self-signed certificates or testing environments
- API error messages are shown as-is to facilitate troubleshooting.

---

**WSO2 API Manager - LLM Gateway** 
