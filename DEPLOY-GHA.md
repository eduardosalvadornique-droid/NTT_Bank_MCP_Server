# Despliegue en Azure Container Apps

Guía para desplegar el servidor FastMCP en el entorno Azure existente del resource group **DefaultResourceGroup-EUS**.

## Recursos del entorno

| Recurso | Tipo | Región |
|---|---|---|
| `nttmcppocacr` | Container Registry | East US |
| `nttmcppoc-environment` | Container Apps Environment | East US |
| `nttmcppoc-app` | Container App | East US |
| `law-container-apps` | Log Analytics Workspace | East US |

---

## Prerrequisitos

- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) instalado
- Acceso al resource group `DefaultResourceGroup-EUS`

---

## Pasos de despliegue

### 1. Hacer un cambio en la rama develop

Realiza el cambio en el MCP server y haz push a la rama develop para activar el workflow de GitHub Actions que construirá y desplegará la nueva imagen automáticamente.

### 2. Iniciar sesión en Azure

```bash
az login
```

### 3. Seleccionar la suscripción correcta

```bash
az account set --subscription "<SUBSCRIPTION_ID>"
```

### 4. Actualizar la Container App con la nueva imagen (referencia el tag)

```bash
az containerapp update --name nttmcppoc-app --resource-group DefaultResourceGroup-EUS --image nttmcppocacr.azurecr.io/nttbank-mcp-server:b502ee38f055c7bda07818f2c7fbdd9e1eaf2ab3
```

### 5. Verifica el mcp server con el inspector de MCP

```bash
npx @modelcontextprotocol/inspector
```

**Nota:** Usa https://nttmcppoc-app.salmonrock-f475cfb8.eastus.azurecontainerapps.io/mcp y el protocolo http-streamable.

---

## Verificación

### Obtener la URL de la aplicación

```bash
az containerapp show \
  --name nttmcppoc-app \
  --resource-group DefaultResourceGroup-EUS \
  --query "properties.configuration.ingress.fqdn" -o tsv
```

### Comprobar que el servidor responde

```bash
curl https://<FQDN>/mcp
```

---

## Ver logs de la aplicación

```bash
az containerapp logs show \
  --name nttmcppoc-app \
  --resource-group DefaultResourceGroup-EUS \
  --type console \
  --follow
```

---

## Comandos útiles

| Acción | Comando |
|---|---|
| Ver estado de la app | `az containerapp show -n nttmcppoc-app -g DefaultResourceGroup-EUS -o table` |
| Reiniciar revisión activa | `az containerapp revision restart -n nttmcppoc-app -g DefaultResourceGroup-EUS --revision <REVISION>` |
| Listar revisiones | `az containerapp revision list -n nttmcppoc-app -g DefaultResourceGroup-EUS -o table` |
| Escalar manualmente | `az containerapp update -n nttmcppoc-app -g DefaultResourceGroup-EUS --min-replicas 1 --max-replicas 5` |
| Ver imágenes en ACR | `az acr repository list --name nttmcppocacr -o table` |
