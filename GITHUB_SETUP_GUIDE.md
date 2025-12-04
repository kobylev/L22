# GitHub Setup Guide - Make Repository Public

## 🚀 Quick Setup

Follow these steps to create a public GitHub repository:

---

## Step 1: Create GitHub Repository

### Option A: Via GitHub Website (Recommended)

1. **Go to GitHub**: https://github.com/new

2. **Repository Details**:
   - **Repository name**: `context-windows-lab`
   - **Description**: `Context Windows Laboratory - Practical experiments demonstrating LLM context window phenomena`
   - **Visibility**: ✅ **Public**
   - **Initialize**: ❌ Do NOT add README, .gitignore, or license (we have them)

3. **Click**: "Create repository"

---

### Option B: Via GitHub CLI

```bash
# Install GitHub CLI first (if not installed)
# https://cli.github.com/

# Create public repository
gh repo create context-windows-lab --public --description "Context Windows Laboratory - Practical LLM experiments"
```

---

## Step 2: Add Files to Git

```bash
cd c:\Ai_Expert\L22

# Check what will be committed
git status

# Add all files (respects .gitignore)
git add .

# Check what's staged
git status
```

---

## Step 3: Create Initial Commit

```bash
# Create first commit
git commit -m "Initial commit: Context Windows Laboratory

- 4 complete experiments demonstrating LLM phenomena
- Lost in the Middle, Context Size Impact, RAG, Engineering Strategies
- Comprehensive documentation and configuration
- Professional visualizations and metrics
- Educational code with clean architecture

🤖 Generated with Claude Code"
```

---

## Step 4: Connect to GitHub

After creating the repository on GitHub, connect it:

```bash
# Add GitHub as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/context-windows-lab.git

# Or with SSH
git remote add origin git@github.com:YOUR_USERNAME/context-windows-lab.git

# Verify remote
git remote -v
```

---

## Step 5: Push to GitHub

```bash
# Push to GitHub (first time)
git push -u origin master

# Or if using 'main' branch
git branch -M main
git push -u origin main
```

---

## 🔐 Before Pushing - Security Check

### ✅ Verify .gitignore is Working

```bash
# Check what will be pushed
git status

# These should NOT appear (they're in .gitignore):
# - .env (contains your settings)
# - __pycache__/
# - *.pyc
# - src/data/results/ (experiment outputs)
# - venv/

# These SHOULD appear:
# - .env.example (template for others)
# - src/ (all code)
# - README.md
# - requirements.txt
```

### ✅ Check .env is Ignored

```bash
# This should show .env in gitignore
cat .gitignore | grep .env

# This should NOT list .env
git status
```

---

## 📝 What Gets Pushed

### ✅ Files Included (Public):
- ✅ All source code (`src/`)
- ✅ Documentation (README.md, guides)
- ✅ `.env.example` (template)
- ✅ requirements.txt
- ✅ .gitignore
- ✅ Configuration files

### ❌ Files Excluded (Private):
- ❌ `.env` (your personal settings)
- ❌ `__pycache__/` (Python cache)
- ❌ `venv/` (virtual environment)
- ❌ `src/data/results/` (experiment outputs)
- ❌ `.vscode/`, `.idea/` (IDE settings)

---

## 🎨 Customize Repository

### Add Topics (on GitHub)

Go to your repository → About → Settings → Add topics:
- `python`
- `machine-learning`
- `llm`
- `context-window`
- `rag`
- `education`
- `ai`
- `experiments`

---

### Add Repository Description

**Description**:
```
Context Windows Laboratory - Practical experiments demonstrating LLM context window phenomena (Lost in the Middle, RAG, Context Engineering)
```

**Website**: (optional)
```
https://github.com/YOUR_USERNAME/context-windows-lab
```

---

## 📄 License (Optional but Recommended)

### Add MIT License

Create `LICENSE` file:

```bash
# Via GitHub web interface
# Settings → Add license → Choose MIT License

# Or manually create LICENSE file
```

**Suggested License**: MIT (permissive, educational-friendly)

---

## 🌟 Make it Discoverable

### 1. Add a Banner Image

Create `docs/banner.png` with:
- Project title
- Key features
- Experiment visualizations

### 2. Add Badges to README

At the top of README.md, add:

```markdown
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
```

### 3. Enable GitHub Pages (Optional)

For documentation hosting:
- Settings → Pages
- Source: Deploy from `main` branch
- Folder: `/` (root)

---

## 🔄 Update Repository Later

### Add New Changes

```bash
# After making changes
git add .
git commit -m "Description of changes"
git push
```

### Create Releases

```bash
# Tag a release
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0

# Or via GitHub: Releases → Create new release
```

---

## 📊 Repository Structure

Your public repository will look like:

```
context-windows-lab/
├── README.md                          # Main documentation
├── LICENSE                            # MIT License
├── requirements.txt                   # Dependencies
├── .gitignore                         # Ignore rules
├── .env.example                       # Config template
├── ENV_CONFIGURATION_GUIDE.md         # Config docs
├── IMPLEMENTATION_SUMMARY.md          # Project summary
├── context_windows_lab_prd.md         # PRD document
├── test_config.py                     # Test script
├── src/
│   ├── main.py                        # CLI entry point
│   ├── experiments/                   # 4 experiments
│   │   ├── experiment1_needle_haystack.py
│   │   ├── experiment2_context_size.py
│   │   ├── experiment3_rag_impact.py
│   │   └── experiment4_engineering.py
│   └── utils/                         # Utilities
│       ├── config.py
│       ├── env_loader.py
│       ├── text_generator.py
│       ├── metrics.py
│       └── visualization.py
└── tests/                             # (future)
```

---

## 🎯 Complete Command Sequence

Here's the full sequence to make it public:

```bash
# 1. Navigate to project
cd c:\Ai_Expert\L22

# 2. Check Git status
git status

# 3. Add all files
git add .

# 4. Create commit
git commit -m "Initial commit: Context Windows Laboratory"

# 5. Create GitHub repo (via website or CLI)
# Go to: https://github.com/new
# Name: context-windows-lab
# Visibility: Public
# Click: Create repository

# 6. Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/context-windows-lab.git

# 7. Push to GitHub
git push -u origin master
```

---

## ✅ Verification

After pushing, check:

1. **Repository is visible**: https://github.com/YOUR_USERNAME/context-windows-lab
2. **README displays**: Should show formatted README.md
3. **Files are correct**: Check src/, docs/, etc.
4. **`.env` is NOT visible**: Verify it's excluded
5. **Stars/Watching**: Enable to track interest

---

## 🌐 Share Your Repository

Once public, share via:

```
Repository URL:
https://github.com/YOUR_USERNAME/context-windows-lab

Clone command:
git clone https://github.com/YOUR_USERNAME/context-windows-lab.git

Installation:
git clone https://github.com/YOUR_USERNAME/context-windows-lab.git
cd context-windows-lab
pip install -r requirements.txt
python src/main.py --experiment all
```

---

## 📧 Collaboration

### Enable Issues

Settings → Features → ✅ Issues

### Enable Discussions

Settings → Features → ✅ Discussions

### Add Contributing Guidelines

Create `CONTRIBUTING.md`:

```markdown
# Contributing to Context Windows Lab

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

See README.md for setup instructions.
```

---

## 🎉 You're Done!

Your Context Windows Laboratory is now public and ready to share!

**Next steps:**
- ⭐ Star your own repo (shows support)
- 📢 Share on LinkedIn, Twitter
- 📝 Write a blog post about it
- 🎓 Add to your portfolio

---

## 🆘 Troubleshooting

### Issue: `.env` is being tracked

```bash
# Remove from Git (keeps local file)
git rm --cached .env

# Add to .gitignore (already done)
echo ".env" >> .gitignore

# Commit the change
git commit -m "Remove .env from tracking"
git push
```

### Issue: Large files error

```bash
# Check file sizes
git ls-files -s | sort -k 2 -n -r | head -10

# Remove large files
git rm --cached path/to/large/file
```

### Issue: Wrong branch name

```bash
# Rename branch to main
git branch -M main
git push -u origin main
```

---

**Happy Sharing! 🚀**
