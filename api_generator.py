from openapi_schema_pydantic import OpenAPI
from openapi_schema_pydantic.util import PydanticSchema, construct_open_api_with_schema_class

from api_schema import CpuAverageLoadResponse, CpuAverageCoreResponse


def construct_base_open_api() -> OpenAPI:
    return OpenAPI.parse_obj({
        "info": {"title": "My own API", "version": "v0.0.1"},
        "paths": {
            "/load": {
                "get": {
                    # "requestBody": {"content": {"application/json": {
                    #     "schema": PydanticSchema(schema_class=PingRequest)
                    # }}},
                    "responses": {"200": {
                        "description": "Average load per minutes",
                        "content": {"application/json": {
                            "schema": PydanticSchema(schema_class=CpuAverageLoadResponse)
                        }},
                    }},
                }
            },
            "/core": {
                "get": {
                    "responses": {"200": {
                        "description": "List of average CPU load per core",
                        "content": {"application/json": {
                            "schema": PydanticSchema(schema_class=CpuAverageCoreResponse)
                        }},
                    }},
                }
            },
            "/health": {
                "get": {
                    "responses": {"200": {
                        "description": "Response server is alive",
                    }},
                }
            }
        },
    })


open_api = construct_base_open_api()
open_api = construct_open_api_with_schema_class(open_api)

if __name__ == '__main__':
    # print the result openapi.json
    print(open_api.json(by_alias=True, exclude_none=True, indent=4))
