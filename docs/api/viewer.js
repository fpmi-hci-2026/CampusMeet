(function () {
    'use strict';
    const spec = window.CampusMeetOpenAPI;
    const container = document.getElementById('operations');
    if (!spec || !container) return;
    Object.entries(spec.paths).forEach(([path, methods]) => {
        Object.entries(methods).forEach(([method, operation]) => {
            const article = document.createElement('article');
            article.className = 'contract-row';
            const title = document.createElement('h2');
            const route = document.createElement('code');
            route.textContent = method.toUpperCase() + ' /api/v1' + path;
            title.append(route);
            const description = document.createElement('p');
            description.textContent = operation.description;
            const details = document.createElement('details');
            const summary = document.createElement('summary');
            summary.textContent = 'Параметры, тело запроса и ответы';
            const pre = document.createElement('pre');
            pre.textContent = JSON.stringify({ parameters: operation.parameters, requestBody: operation.requestBody, responses: operation.responses }, null, 2);
            details.append(summary, pre);
            article.append(title, description, details);
            container.append(article);
        });
    });
    if (typeof window.SwaggerUIBundle === 'function') {
        window.SwaggerUIBundle({ spec, dom_id: '#swagger-ui', deepLinking: true, validatorUrl: null, supportedSubmitMethods: ['get', 'post', 'put', 'patch', 'delete'] });
        document.getElementById('offline-contract').open = false;
    }
})();
