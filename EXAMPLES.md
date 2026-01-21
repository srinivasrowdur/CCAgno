# Smart Architecture Diagram Creator - Examples

## Example System Descriptions

### 1. E-commerce Platform
```
A scalable e-commerce platform with microservices architecture including:
- User authentication service (OAuth 2.0, JWT tokens)
- Product catalog service (ElasticSearch for search)
- Shopping cart service (Redis for session management)
- Payment processing gateway (Stripe, PayPal integration)
- Order management service (PostgreSQL database)
- Notification service (Email, SMS, Push notifications)
- API Gateway (Kong/AWS API Gateway)
- Load Balancer (NGINX)
- Cloud storage (AWS S3 for product images)
- Message Queue (RabbitMQ for async processing)
```

### 2. Real-time Chat Application
```
A real-time chat application with:
- WebSocket connections for real-time messaging
- Message queue (Kafka) for async processing
- User presence tracking (Redis)
- File sharing service (S3)
- Message history database (MongoDB)
- User authentication (Firebase Auth)
- Redis for caching
- Media server for voice/video calls
- CDN for static assets
```

### 3. Machine Learning Pipeline
```
An end-to-end ML pipeline for image classification:
- Data ingestion layer (Apache Airflow)
- Data preprocessing service (Python/Spark)
- Feature engineering pipeline
- Model training infrastructure (GPU clusters, Kubernetes)
- Model registry (MLflow)
- Model serving API (FastAPI, TensorFlow Serving)
- Monitoring and logging (Prometheus, Grafana)
- A/B testing framework
- Feedback loop for continuous learning
- Cloud storage (S3/GCS) for datasets and models
```

### 4. Serverless Data Processing System
```
A serverless architecture for data processing:
- AWS Lambda functions for compute
- S3 for data storage
- DynamoDB for metadata
- Step Functions for workflow orchestration
- EventBridge for event routing
- Kinesis for streaming data
- Glue for ETL jobs
- Athena for querying
- CloudWatch for monitoring
```

### 5. Microservices-based Social Media Platform
```
A social media platform with microservices:
- User service (authentication, profiles)
- Post service (create, read, update posts)
- Feed service (personalized feed generation)
- Comment service (threaded comments)
- Like/Reaction service
- Notification service
- Media processing service (image/video upload)
- Search service (Elasticsearch)
- Recommendation engine
- Analytics service
- API Gateway
- Service mesh (Istio)
- Distributed caching (Redis Cluster)
- Message broker (Kafka)
```

### 6. IoT Platform
```
An IoT platform for device management:
- Device registry and management
- MQTT broker for device communication
- Time-series database (InfluxDB)
- Stream processing (Apache Flink)
- Analytics dashboard (Grafana)
- Alert and notification system
- Device firmware update service
- Authentication and authorization (OAuth2)
- Data lake for historical data
- Machine learning for predictive maintenance
```

## Tips for Writing Good Descriptions

1. **Be Specific**: Include specific technologies and services
2. **Include Components**: List all major components and services
3. **Mention Integrations**: Specify external services and APIs
4. **Data Flow**: Describe how data flows between components
5. **Scalability**: Mention scaling strategies if relevant
6. **Security**: Include authentication and security measures

## Expected Output

When you submit a description, the AI will generate:
1. A comprehensive architecture analysis
2. Component breakdown
3. Relationships and data flows
4. Best practices and recommendations
5. A text-based architecture diagram

## Note on API Usage

This application requires a valid Google API key with access to the Gemini API. The key should be:
- Stored in the `.env` file as `GOOGLE_API_KEY=your_key_here`, OR
- Entered directly in the Streamlit sidebar
