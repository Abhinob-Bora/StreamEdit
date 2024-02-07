project/
│
├── server/               # Backend folder
│   ├── app.py             # Main Flask application file
│   ├── requirements.txt   # File listing required Python libraries
│   ├── config.py          # Configuration settings for the backend
│   │
│   ├── api/               # API routes
│   │   ├── __init__.py    # Package initializer
│   │   ├── overlays.py    # Routes for CRUD operations on overlays
│   │   └── livestream.py  # Route for playing livestream
│   │
│   ├── models/            # Data models
│   │   ├── __init__.py    # Package initializer
│   │   └── overlay.py     # Definition of Overlay model
│   │
│   └── utils/             # Utility functions
│       ├── __init__.py    # Package initializer
│       └── mongo.py       # MongoDB setup and helper functions
│
└── client/              # Frontend folder
    ├── public/            # Public assets
    ├── src/               # Source code
    │   ├── components/    # React components
    │   ├── pages/         # React pages
    │   ├── services/      # Services for API interaction
    │   ├── App.css        # Global styles
    │   ├── App.js         # Main React application file
    │   └── index.js       # Entry point for React application
    │
    ├── package.json       # Package configuration for frontend
    └── README.md          # Frontend-specific documentation
