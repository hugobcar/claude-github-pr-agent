"""
Example Python module to test Claude Code Review workflow.
This module implements a simple user management system.
"""

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """Represents a user in the system."""

    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime
    is_active: bool = True


class UserRepository:
    """Handles user data persistence and retrieval."""

    def __init__(self, storage_path: str = "users.json"):
        self.storage_path = storage_path
        self._users: dict[int, User] = {}
        self._next_id = 1
        self._load_users()

    def _load_users(self) -> None:
        """Load users from storage file."""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for user_data in data:
                    user = User(
                        id=user_data["id"],
                        username=user_data["username"],
                        email=user_data["email"],
                        password_hash=user_data["password_hash"],
                        created_at=datetime.fromisoformat(user_data["created_at"]),
                        is_active=user_data.get("is_active", True),
                    )
                    self._users[user.id] = user
                    self._next_id = max(self._next_id, user.id + 1)

    def _save_users(self) -> None:
        """Persist users to storage file."""
        data = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password_hash": user.password_hash,
                "created_at": user.created_at.isoformat(),
                "is_active": user.is_active,
            }
            for user in self._users.values()
        ]
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def create(self, username: str, email: str, password: str) -> User:
        """Create a new user."""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = User(
            id=self._next_id,
            username=username,
            email=email,
            password_hash=password_hash,
            created_at=datetime.now(),
        )
        self._users[user.id] = user
        self._next_id += 1
        self._save_users()
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
        return self._users.get(user_id)

    def get_by_username(self, username: str) -> Optional[User]:
        """Retrieve a user by their username."""
        for user in self._users.values():
            if user.username == username:
                return user
        return None

    def update(self, user: User) -> None:
        """Update an existing user."""
        if user.id not in self._users:
            raise ValueError(f"User with id {user.id} not found")
        self._users[user.id] = user
        self._save_users()

    def delete(self, user_id: int) -> bool:
        """Delete a user by their ID."""
        if user_id in self._users:
            del self._users[user_id]
            self._save_users()
            return True
        return False

    def list_all(self) -> list[User]:
        """Return all users."""
        return list(self._users.values())


class AuthenticationService:
    """Handles user authentication."""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Authenticate a user with username and password."""
        user = self.user_repository.get_by_username(username)
        if user is None:
            return None

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash == password_hash and user.is_active:
            return user
        return None

    def register(self, username: str, email: str, password: str) -> User:
        """Register a new user."""
        if self.user_repository.get_by_username(username):
            raise ValueError(f"Username '{username}' already exists")

        if not self._validate_email(email):
            raise ValueError("Invalid email format")

        if not self._validate_password(password):
            raise ValueError("Password must be at least 8 characters")

        return self.user_repository.create(username, email, password)

    def _validate_email(self, email: str) -> bool:
        """Basic email validation."""
        return "@" in email and "." in email.split("@")[-1]

    def _validate_password(self, password: str) -> bool:
        """Validate password strength."""
        return len(password) >= 8


def main() -> None:
    """Example usage of the user management system."""
    repo = UserRepository("example_users.json")
    auth_service = AuthenticationService(repo)

    # Register a new user
    try:
        user = auth_service.register(
            username="johndoe",
            email="john@example.com",
            password="securepassword123",
        )
        print(f"User created: {user.username} (ID: {user.id})")
    except ValueError as e:
        print(f"Registration failed: {e}")

    # Authenticate user
    authenticated_user = auth_service.authenticate("johndoe", "securepassword123")
    if authenticated_user:
        print(f"Authentication successful for: {authenticated_user.username}")
    else:
        print("Authentication failed")

    # List all users
    all_users = repo.list_all()
    print(f"Total users: {len(all_users)}")


if __name__ == "__main__":
    main()
