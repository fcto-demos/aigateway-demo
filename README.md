# WSO2 API Manager - AI Gateway

This application is a Streamlit interface to interact with LLM models (such as OpenAI, Mistral, and Anthropic) through a WSO2 API Gateway, featuring OAuth2 authentication, multiple application management, predefined prompts, and provider selection capabilities.

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
- Python 3.8+
- The libraries listed in `requirements.txt` (Streamlit, requests, PyYAML, etc.)

## Prerequisites

Before installing the application, you need to set up access to the WSO2 API Gateway:

### WSO2 Developer Portal Setup

1. **Access the WSO2 Developer Portal**
   - Navigate to your WSO2 API Manager Developer Portal
   - Log in with your developer account

2. **Create a New Application**
   - Go to "Applications" section
   - Click "Add Application"
   - Fill in the application details:
     - **Name**: e.g., "LLM Gateway Client"
     - **Per Token Quota**: Set according to your usage needs
     - **Description**: "Application for accessing LLM APIs through WSO2 Gateway"
   - Click "Add" to create the application

3. **Subscribe to LLM APIs**
   Subscribe your application to all available LLM APIs:
   - **OpenAI API**: Subscribe to the OpenAI chat completions endpoint
   - **Mistral AI API**: Subscribe to the Mistral chat completions endpoint
   - **Anthropic API**: Subscribe to the Anthropic messages endpoint
   - Any other LLM APIs available in your WSO2 instance

4. **Generate Application Credentials**
   - Go to your application's "Production Keys" tab
   - Click "Generate Keys" to create OAuth2 credentials
   - Copy the **Consumer Key** and **Consumer Secret**
   - Note the **Token URL** (typically `https://your-wso2-server:9443/oauth2/token`)

5. **Get API Endpoints**
   - For each subscribed API, note the gateway endpoint URLs
   - These are typically in the format: `https://your-wso2-server:8243/{api-context}/{version}`

## Installation

1. Clone the repository or download the files.
2. Create a virtual environment and install the dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Configure your environment:
   - Copy `.env.example` to `.env` and fill in your WSO2 credentials
   - Review and customize `config.yaml` for provider settings
   - Review and customize `applications.yaml` for application management
   - Optionally customize `prompts.yaml` for predefined test prompts



## Configuration

The application uses three main configuration files:

### 1. Environment Variables (`.env` file)
Sensitive credentials are stored in a `.env` file that is not tracked by git. Supports both shared and application-specific credentials:

```env
# Shared WSO2 Gateway Credentials (Required - fallback for all applications)
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
    # USER_AGENT: "Custom-Anthropic-Client/1.0"  # Optional: provider-specific User-Agent override
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
    providers: ["OPENLLM", "MISTRAL"]
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

### Adding a New Provider
1. **Subscribe to the new LLM API** in your WSO2 Developer Portal application
2. **Get the API endpoint** from the WSO2 Developer Portal
3. **Add the chat completions URL** to `.env` following the `{PROVIDER_NAME}_CHAT_COMPLETIONS_URL` pattern
4. **Add a new entry** under `providers:` in `config.yaml` with `MODEL`, `DESCRIPTION`, and `ENABLED` fields
5. **Update application access** in `applications.yaml` to grant provider access to specific applications
6. No code changes are needed: the app automatically detects the defined providers

Example for adding a new "GEMINI" provider:
1. Subscribe to Gemini API in WSO2 Developer Portal
2. Add the endpoint URL to `.env`:
   ```env
   GEMINI_CHAT_COMPLETIONS_URL=https://your-wso2-server:8243/geminiapi/v1/chat/completions
   ```
3. Add the provider to `config.yaml`:
   ```yaml
   GEMINI:
     MODEL: "gemini-pro"
     DESCRIPTION: "Google Gemini Pro - Multimodal AI model"
     ENABLED: true
   ```
4. Update your application in `applications.yaml` to grant access:
   ```yaml
   mobile:
     name: "Mobile App"
     description: "Mobile application"
     enabled: true
     providers: ["OPENLLM", "MISTRAL", "GEMINI"]  # Added GEMINI
   ```

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

### Adding Predefined Prompts
Add new entries to `prompts.yaml`:
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

### How Localization Works

The localization system consists of two main components:

1. **UI Translations** ([localization.py](localization.py)) - Handles all interface text including labels, buttons, messages, and error text
2. **Prompt Translations** (`prompts_{lang}.yaml`) - Provides localized versions of predefined test prompts

### Adding a New Language

To add support for a new language (e.g., French), follow these steps:

#### 1. Add UI Translations

Edit [localization.py](localization.py) and add a new language entry to the `TRANSLATIONS` dictionary:

```python
TRANSLATIONS = {
    'en': {
        'title': "API Manager - AI Gateway Demo",
        'select_provider': "Select the provider:",
        # ... other English translations
    },
    'es': {
        # ... Spanish translations
    },
    'fr': {  # Add new language
        'title': "API Manager - AI Gateway Demo",
        'select_provider': "Sélectionnez le fournisseur:",
        'select_prompt': "Sélectionnez une invite:",
        'ask_question': "Posez une question à {provider}",
        'response_from': "Réponse de {provider}",
        'send': "Envoyer",
        'success_count': "Appels réussis à {provider}: {count}",
        'error_count': "Appels échoués à {provider}: {count}",
        # ... translate all other keys
    }
}
```

**Important:** Ensure you translate ALL keys present in the 'en' dictionary. Missing keys will fallback to the key name itself.

**Translation Tips:**
- Maintain the same placeholder variables (e.g., `{provider}`, `{count}`, `{app}`) in your translations
- Keep technical terms consistent (e.g., "SSL/TLS", "OAuth2")
- Test special characters and accents in the Streamlit UI

#### 2. Add Prompt Translations

Create a new prompts file for your language (e.g., `prompts_fr.yaml`):

```yaml
# Prompts predefined pour la demo (français)
prompts:
  - name: "Vérifier le moteur IA"
    text: "Quel modèle d'IA êtes-vous?"
  - name: "Test de garde sémantique"
    text: "Pouvez-vous expliquer l'histoire du football?"
  # ... translate all prompts from prompts.yaml
```

**Prompt Translation Guidelines:**
- Keep the same order and number of prompts as the original `prompts.yaml`
- Translate both the `name` (displayed in the UI) and `text` (sent to the LLM)
- Maintain the intent of each test prompt (e.g., semantic guards, PII detection tests)

#### 3. Update Language Selection Logic

The application automatically detects available languages from the `TRANSLATIONS` dictionary in [localization.py](localization.py). Once you've added the new language, it will appear in the language selector dropdown in the sidebar.

The prompt file loading is handled automatically based on the selected language:
- `prompts.yaml` → English (default)
- `prompts_es.yaml` → Spanish
- `prompts_fr.yaml` → French (your new language)

If a language-specific prompt file doesn't exist, the application falls back to `prompts.yaml`.

#### 4. Testing Your Translation

After adding a new language:

1. Start the application: `streamlit run demo_ui.py`
2. Select your new language from the sidebar dropdown
3. Verify all UI elements are translated correctly
4. Check that predefined prompts load from your new `prompts_{lang}.yaml` file
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
| `missing_fields` | Config error message | "Missing the following fields in provider config: {fields}" |
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