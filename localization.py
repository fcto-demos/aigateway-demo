TRANSLATIONS = {
    'en': {
        'title': "API Manager - AI Gateway Demo",
        'select_provider': "Select the provider:",
        'select_prompt': "Select a prompt:",
        'ask_question': "Ask a question to {provider}",
        'response_from': "Response from {provider}",
        'send': "Send",
        'success_count': "Successful calls to {provider}: {count}",
        'error_count': "Failed calls to {provider}: {count}",
        'select_and_ask': "Select the provider and ask your question.",
        'missing_provider_fields': "Missing the following fields in provider config: {fields} (for provider {provider})",
        'missing_app_fields': "Missing the following fields in application config: {fields} (for application {app})",
        'no_access_token': "Could not obtain access token.",
        'token_error': "Error obtaining token. Status: {status}",
        'unknown_error': "Unknown error.",
        'api_request_error': "Error making API request: {error}",
        'blocked_url': "Response blocked due to invalid or inaccessible URL: {urls}",
        'default_question': "Who are you?",
        'env_config_help': "Please ensure your .env file contains the required credentials. See .env.example for reference.",
        'empty_question_error': "Please enter a question before sending.",
        'question_too_long': "Question is too long. Maximum {max_length} characters allowed.",
        'tls_disabled_warning': "⚠️ SSL/TLS verification is DISABLED. Connections are NOT secure!",
        'tls_enabled_status': "🔒 SSL/TLS verification is ENABLED. Connections are secure.",
        'tls_status_label': "Security Status",
        'select_application': "Select application:",
        'app_provider_success': "Successful calls from {app} to {provider}: {count}",
        'app_provider_error': "Failed calls from {app} to {provider}: {count}",
        'no_applications_available': "No applications are configured or enabled.",
        'no_providers_for_app': "No providers are available for the selected application.",
        'token_count': "Prompt tokens: {count}",
    },
    'es': {
        'title': "API Manager - AI Gateway Demo",
        'select_provider': "Selecciona el proveedor:",
        'select_prompt': "Selecciona un prompt:",
        'ask_question': "Haz una pregunta a {provider}",
        'response_from': "Respuesta de {provider}",
        'send': "Enviar",
        'success_count': "Llamadas exitosas a {provider}: {count}",
        'error_count': "Llamadas incorrectas a {provider}: {count}",
        'select_and_ask': "Selecciona el proveedor y haz tu pregunta.",
        'missing_provider_fields': "Faltan los siguientes campos en la configuración del proveedor: {fields} (para proveedor {provider})",
        'missing_app_fields': "Faltan los siguientes campos en la configuración de la aplicación: {fields} (para aplicación {app})",
        'no_access_token': "No se pudo obtener el access token.",
        'token_error': "Error al obtener token. Estado: {status}",
        'unknown_error': "Error desconocido.",
        'api_request_error': "Error al realizar la solicitud a la API: {error}",
        'blocked_url': "Se ha bloqueado la respuesta por contener una URL inválida o no accesible: {urls}",
        'default_question': "Hola! ¿quién eres?",
        'env_config_help': "Por favor asegúrate de que tu archivo .env contiene las credenciales requeridas. Consulta .env.example como referencia.",
        'empty_question_error': "Por favor ingresa una pregunta antes de enviar.",
        'question_too_long': "La pregunta es demasiado larga. Máximo {max_length} caracteres permitidos.",
        'tls_disabled_warning': "⚠️ La verificación SSL/TLS está DESHABILITADA. ¡Las conexiones NO son seguras!",
        'tls_enabled_status': "🔒 La verificación SSL/TLS está HABILITADA. Las conexiones son seguras.",
        'tls_status_label': "Estado de Seguridad",
        'select_application': "Selecciona la aplicación:",
        'app_provider_success': "Llamadas exitosas de {app} a {provider}: {count}",
        'app_provider_error': "Llamadas incorrectas de {app} a {provider}: {count}",
        'no_applications_available': "No hay aplicaciones configuradas o habilitadas.",
        'no_providers_for_app': "No hay proveedores disponibles para la aplicación seleccionada.",
        'token_count': "Prompt tokens: {count}",
    },
    'nl': {
        'title': "API Manager - AI Gateway Demo",
        'select_provider': "Selecteer de provider:",
        'select_prompt': "Selecteer een prompt:",
        'ask_question': "Stel een vraag aan {provider}",
        'response_from': "Antwoord van {provider}",
        'send': "Versturen",
        'success_count': "Succesvolle oproepen naar {provider}: {count}",
        'error_count': "Mislukte oproepen naar {provider}: {count}",
        'select_and_ask': "Selecteer de provider en stel je vraag.",
        'missing_provider_fields': "De volgende velden ontbreken in de provider configuratie: {fields} (voor provider {provider})",
        'missing_app_fields': "De volgende velden ontbreken in de applicatie configuratie: {fields} (voor applicatie {app})",
        'no_access_token': "Kon geen access token verkrijgen.",
        'token_error': "Fout bij het verkrijgen van token. Status: {status}",
        'unknown_error': "Onbekende fout.",
        'api_request_error': "Fout bij het maken van API verzoek: {error}",
        'blocked_url': "Antwoord geblokkeerd vanwege ongeldige of niet toegankelijke URL: {urls}",
        'default_question': "Wie ben je?",
        'env_config_help': "Zorg ervoor dat je .env bestand de vereiste credentials bevat. Zie .env.example als referentie.",
        'empty_question_error': "Voer een vraag in voordat je verzendt.",
        'question_too_long': "Vraag is te lang. Maximaal {max_length} tekens toegestaan.",
        'tls_disabled_warning': "⚠️ SSL/TLS verificatie is UITGESCHAKELD. Verbindingen zijn NIET veilig!",
        'tls_enabled_status': "🔒 SSL/TLS verificatie is INGESCHAKELD. Verbindingen zijn veilig.",
        'tls_status_label': "Beveiligingsstatus",
        'select_application': "Selecteer applicatie:",
        'app_provider_success': "Succesvolle oproepen van {app} naar {provider}: {count}",
        'app_provider_error': "Mislukte oproepen van {app} naar {provider}: {count}",
        'no_applications_available': "Geen applicaties zijn geconfigureerd of ingeschakeld.",
        'no_providers_for_app': "Geen providers beschikbaar voor de geselecteerde applicatie.",
        'token_count': "Prompt tokens: {count}",
    }
}

_current_lang = 'en'

def set_lang(lang):
    global _current_lang
    if lang in TRANSLATIONS:
        _current_lang = lang
    else:
        _current_lang = 'en'

def get_lang():
    return _current_lang

def t(key, **kwargs):
    txt = TRANSLATIONS.get(_current_lang, TRANSLATIONS['en']).get(key, key)
    return txt.format(**kwargs) if kwargs else txt
