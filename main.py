# ===============================
# Netflix Movies & TV Shows EDA
# Author: Garishma
# ===============================

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
print("Loading dataset...\n")

df = pd.read_csv("netflix_titles.csv")

print("Dataset Loaded Successfully!\n")

# -------------------------------
# Basic Information
# -------------------------------
print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

print("\n")

print("=" * 50)
print("Dataset Information")
print("=" * 50)
print(df.info())

print("\n")

print("=" * 50)
print("Shape of Dataset")
print("=" * 50)
print(df.shape)

print("\n")

# -------------------------------
# Missing Values
# -------------------------------
print("=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["date_added"] = df["date_added"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

print("\nMissing values handled successfully.\n")

# -------------------------------
# Check Data Types
# -------------------------------
print("=" * 50)
print("Data Types")
print("=" * 50)
print(df.dtypes)

print("\n")

# -------------------------------
# Duplicate Values
# -------------------------------
duplicates = df.duplicated().sum()

print("=" * 50)
print("Duplicate Rows")
print("=" * 50)
print(duplicates)

df = df.drop_duplicates()

print("Duplicates removed successfully.\n")

# -------------------------------
# Summary Statistics
# -------------------------------
print("=" * 50)
print("Summary Statistics")
print("=" * 50)
print(df.describe(include="all"))

# -------------------------------
# Movies vs TV Shows
# -------------------------------
type_counts = df["type"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(type_counts.index, type_counts.values)
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

# -------------------------------
# Ratings Distribution
# -------------------------------
rating_counts = df["rating"].value_counts().head(10)

plt.figure(figsize=(8,5))
plt.bar(rating_counts.index, rating_counts.values)
plt.title("Top 10 Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ratings_distribution.png")
plt.show()

# -------------------------------
# Top 10 Countries
# -------------------------------
country_counts = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.bar(country_counts.index, country_counts.values)
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")
plt.show()

# -------------------------------
# Content Added Per Year
# -------------------------------
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

year_counts = (
    df["date_added"]
    .dt.year
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,5))
plt.plot(year_counts.index, year_counts.values, marker="o")
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig("content_added_per_year.png")
plt.show()

# -------------------------------
# Top 10 Genres
# -------------------------------
genre_counts = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,5))
plt.barh(genre_counts.index, genre_counts.values)
plt.title("Top 10 Genres")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

# -------------------------------
# Save Cleaned Dataset
# -------------------------------
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("\nCleaned dataset saved as:")
print("cleaned_netflix_dataset.csv")

print("\nGraphs saved:")
print("1. movies_vs_tvshows.png")
print("2. ratings_distribution.png")
print("3. top_countries.png")
print("4. content_added_per_year.png")
print("5. top_genres.png")

print("\nEDA Completed Successfully!")