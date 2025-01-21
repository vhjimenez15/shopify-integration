# Shopify Integration API

Este proyecto proporciona una API desarrollada con Django Rest Framework (DRF) que se integra con las APIs de Shopify. Permite listar productos, pedidos, inventarios y clientes. Además, implementa un filtro en los pedidos basado en su estado, si están pagados o por el nombre del cliente.

## Características

- **Productos:** Lista los productos registrados en Shopify.
- **Pedidos:** Lista los pedidos de Shopify con la capacidad de filtrarlos por:
  - Estado del pedido. Si están pagados o no.
  - Nombre o clave del articulo.
- **Inventarios:** Lista el inventario disponible.
- **Clientes:** Lista los clientes registrados en Shopify.

---

## Tecnologías utilizadas

- **Python** (Django y DRF)
- **Shopify API**
- **Docker**

---

## Instalación y configuración

### **Prerrequisitos**

1. Tener instalados:
   - [Docker](https://www.docker.com/)
   - [Docker Compose](https://docs.docker.com/compose/)
2. Credenciales de tu tienda Shopify:
   - **API Key** y **API Secret** de una app personalizada.
   - Nombre de tu tienda (subdominio antes de `.myshopify.com`).

### **Configuración**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/shopify-integration.git
   cd shopify-integration
   ```

2. Crea un archivo `.env` en el directorio raíz con las siguientes variables:
   ```env
   SHOPIFY_API_KEY=tu_api_key
   SHOPIFY_API_SECRET=tu_api_secret
   SHOPIFY_STORE=tu_nombre_de_tienda
   ```

3. Construye y ejecuta los contenedores:
   ```bash
   docker compose up --build
   ```

---

## Uso de la API

### **Base URL**
La API está disponible en: `http://localhost:8000/shop/`

### **Endpoints principales**

1. **Productos:**
   - **GET** `/shop/products/`
   - Obtiene una lista de productos desde Shopify.

2. **Pedidos:**
   - **GET** `/shop/orders/`
     - **Parámetros opcionales:**
       - `status`: Filtra por estado del pedido (por ejemplo, `open`, `closed`).
       - `paid`: Filtra si el pedido está pagado (`true` o `false`).
       - `customer_name`: Filtra por el nombre del cliente.

3. **Inventario:**
   - **GET** `/shop/inventory/`
   - Obtiene una lista de inventarios desde Shopify.

4. **Clientes:**
   - **GET** `/shop/customers/`
   - Obtiene una lista de clientes registrados en Shopify.

---

## Notas adicionales

- En el proyecto hay un collectión con postman el cual se usó para la prueba de las APIs
- Las urls no están protejidas o securizadas.
- Asegúrate de configurar correctamente las credenciales en el archivo `.envs`.
- Si necesitas exponer el servicio, actualiza las configuraciones de Docker y el `ALLOWED_HOSTS` en `settings.py`.

---

¡Gracias por usar esta integración con Shopify! Si tienes preguntas, no dudes en contactarme.

