# Security Anti-Patterns to Flag in Reviews

## 1. Secrets & Credentials in Source
- **Pattern**: Hardcoded API keys, private keys, or passwords.
- **Remedy**: Use environment variables or secret management vaults.

## 2. Insecure Direct Object References (IDOR)
- **Pattern**:
  ```python
  # Vulnerable: Accepts document_id directly from query param without checking ownership
  @app.get("/documents/{doc_id}")
  def get_doc(doc_id: int):
      return db.query(Document).filter_by(id=doc_id).first()
  ```
- **Remedy**:
  ```python
  # Safe: Verifies current authenticated user owns the document
  @app.get("/documents/{doc_id}")
  def get_doc(doc_id: int, current_user: User = Depends(get_current_user)):
      doc = db.query(Document).filter_by(id=doc_id, owner_id=current_user.id).first()
      if not doc:
          raise HTTPException(status_code=404)
      return doc
  ```

## 3. Unescaped Output & XSS
- **Pattern**: Inserting user-controlled strings directly into HTML (`innerHTML`, `dangerouslySetInnerHTML`, `v-html`).
- **Remedy**: Use text content bindings or sanitize with trusted libraries (e.g., DOMPurify).

## 4. Path Traversal
- **Pattern**: `open(f"/uploads/{filename}")` where `filename` might contain `../../etc/passwd`.
- **Remedy**: Sanitize using `os.path.basename` and resolve to ensure canonical path is within the target directory.

## 5. ReDoS (Regular Expression Denial of Service)
- **Pattern**: Catastrophic backtracking regex with nested quantifiers like `(a+)+$`.
- **Remedy**: Use linear regex engines, non-backtracking patterns, or explicit string parsing.
