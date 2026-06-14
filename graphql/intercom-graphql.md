# Intercom GraphQL

## Description

Intercom does not publish a public GraphQL API. Its developer platform is built entirely on REST. The GraphQL schema in this directory is a conceptual data model derived from the official Intercom REST API (OpenAPI specification), public documentation at https://developers.intercom.com/docs/, and the documented resource types that underpin the platform.

The schema represents the same entities and relationships exposed through the REST surface — Contacts, Companies, Conversations, Articles, Segments, Admins, Tags, Teams, Events, Notes, ConversationParts, DataAttributes, Webhooks, and Subscriptions — modelled in GraphQL SDL for interoperability, tooling, and data-graph planning purposes.

## Endpoint

No public GraphQL endpoint exists. The REST base URL is:

```
https://api.intercom.io
```

Regional variants:
- US: `https://api.intercom.io`
- EU: `https://api.eu.intercom.io`
- AU: `https://api.au.intercom.io`

## Authentication

Intercom uses Bearer token authentication. Tokens are either personal access tokens (PATs) generated in the developer hub or OAuth 2.0 access tokens issued after completing an OAuth flow for third-party app integrations.

```
Authorization: Bearer <access_token>
```

OAuth 2.0 authorization endpoint: `https://app.intercom.com/oauth`

Documentation: https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/

## Rate Limits

- Standard: ~1000 requests per minute (166 req/10s)
- Search endpoints: ~200 requests per minute (33 req/10s)
- Bulk endpoints: ~100 requests per minute (16 req/10s)

## Notes

- Schema source: conceptual model derived from Intercom REST OpenAPI (`openapi/intercom-openapi.yml`) and public documentation
- Schema status: REST-derived SDL, not from live GraphQL introspection
- Key resource types: Contact, Company, Conversation, ConversationPart, Article, Section, Collection, Admin, Team, Tag, Segment, Event, Note, DataAttribute, Webhook, Subscription
- All timestamps are Unix epoch integers in the REST API; represented as `Int` (epoch) in this SDL
- Pagination in REST uses cursor-based and page-based patterns; modelled here as connection/edge types
- Intercom's AI features (Fin, Copilot) are accessible via REST conversation and message endpoints, not a separate API surface
