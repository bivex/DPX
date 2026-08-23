# 🔍 Software Design Pattern Detection Report

> **Project:** `/Volumes/External/Code/DPX/scratch/repos/ring`  
> **Scanned Files:** 81  
> **Total Detections:** 119  
> **Duration:** 0.859s  

---

## 📊 Summary by Category

| Category | Detections Count |
| :--- | :---: |
| **CREATIONAL** | 7 |
| **STRUCTURAL** | 90 |
| **BEHAVIORAL** | 22 |

---

## 📋 Identified Design Patterns

### #1 TEMPLATE_METHOD on template_bracket `with-locale`
- **Confidence:** 91% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:9:1-13:54`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Template Method: 'with-locale' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+50%** `[TEMPLATE_METHOD_WITH_BRACKET_NAMING]` Follows idiomatic Clojure 'with-*' resource bracket template naming: 'with-locale' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:9:1-13:54`)_
- **+40%** `[TEMPLATE_METHOD_MACRO_BRACKET]` Macro encapsulates algorithmic skeleton expanding user-supplied body expressions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:9:1-13:54`)_
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:9:1-13:54`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (body) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:9:1-13:54`)_

---

### #2 TEMPLATE_METHOD on template_bracket `with-locale`
- **Confidence:** 91% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:8:1-12:54`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Template Method: 'with-locale' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+50%** `[TEMPLATE_METHOD_WITH_BRACKET_NAMING]` Follows idiomatic Clojure 'with-*' resource bracket template naming: 'with-locale' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:8:1-12:54`)_
- **+40%** `[TEMPLATE_METHOD_MACRO_BRACKET]` Macro encapsulates algorithmic skeleton expanding user-supplied body expressions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:8:1-12:54`)_
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:8:1-12:54`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (body) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:8:1-12:54`)_

---

### #3 TEMPLATE_METHOD on template_bracket `with-server`
- **Confidence:** 91% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:58:1-62:35`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- **Summary:** Template Method: 'with-server' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+50%** `[TEMPLATE_METHOD_WITH_BRACKET_NAMING]` Follows idiomatic Clojure 'with-*' resource bracket template naming: 'with-server' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:58:1-62:35`)_
- **+40%** `[TEMPLATE_METHOD_MACRO_BRACKET]` Macro encapsulates algorithmic skeleton expanding user-supplied body expressions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:58:1-62:35`)_
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:58:1-62:35`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (body) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:58:1-62:35`)_

---

### #4 TEMPLATE_METHOD on template_bracket `with-classloader`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/util/test/response.clj:97:1-109:70`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/util/test/response.clj)
- **Summary:** Template Method: 'with-classloader' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+50%** `[TEMPLATE_METHOD_WITH_BRACKET_NAMING]` Follows idiomatic Clojure 'with-*' resource bracket template naming: 'with-classloader' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/util/test/response.clj:97:1-109:70`)_
- **+40%** `[TEMPLATE_METHOD_MACRO_BRACKET]` Macro encapsulates algorithmic skeleton expanding user-supplied body expressions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/util/test/response.clj:97:1-109:70`)_
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/util/test/response.clj:97:1-109:70`)_

---

### #5 TEMPLATE_METHOD on template_bracket `with-last-modified`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/file_info.clj:14:1-22:57`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/file_info.clj)
- **Summary:** Template Method: 'with-last-modified' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+50%** `[TEMPLATE_METHOD_WITH_BRACKET_NAMING]` Follows idiomatic Clojure 'with-*' resource bracket template naming: 'with-last-modified' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/file_info.clj:14:1-22:57`)_
- **+40%** `[TEMPLATE_METHOD_MACRO_BRACKET]` Macro encapsulates algorithmic skeleton expanding user-supplied body expressions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/file_info.clj:14:1-22:57`)_
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/file_info.clj:14:1-22:57`)_

---

### #6 DECORATOR on middleware_decorator `wrap-stacktrace-log`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-stacktrace-log' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-stacktrace-log' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_

---

### #7 DECORATOR on middleware_decorator `wrap-stacktrace-web`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-stacktrace-web' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-stacktrace-web' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_

---

### #8 DECORATOR on middleware_decorator `wrap-reload`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-reload' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-reload' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_

---

### #9 DECORATOR on middleware_decorator `wrap-lint`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj:90:1-107:23`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-lint' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj:90:1-107:23`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj:90:1-107:23`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-lint' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj:90:1-107:23`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/lint.clj:90:1-107:23`)_

---

### #10 DECORATOR on middleware_decorator `wrap-keyword-params`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj:37:1-55:74`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-keyword-params' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj:37:1-55:74`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj:37:1-55:74`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-keyword-params' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj:37:1-55:74`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/keyword_params.clj:37:1-55:74`)_

---

### #11 DECORATOR on middleware_decorator `wrap-resource-prefer-resources`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:21:1-29:42`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-resource-prefer-resources' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:21:1-29:42`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:21:1-29:42`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-resource-prefer-resources' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:21:1-29:42`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:21:1-29:42`)_

---

### #12 DECORATOR on middleware_decorator `wrap-resource-prefer-handler`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:31:1-46:23`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-resource-prefer-handler' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:31:1-46:23`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:31:1-46:23`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-resource-prefer-handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:31:1-46:23`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:31:1-46:23`)_

---

### #13 DECORATOR on middleware_decorator `wrap-multipart-params`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:146:1-200:53`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-multipart-params' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:146:1-200:53`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:146:1-200:53`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-multipart-params' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:146:1-200:53`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:146:1-200:53`)_

---

### #14 DECORATOR on middleware_decorator `wrap-flash`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj:31:1-44:26`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-flash' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj:31:1-44:26`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj:31:1-44:26`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-flash' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj:31:1-44:26`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/flash.clj:31:1-44:26`)_

---

### #15 DECORATOR on middleware_decorator `wrap-params`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:56:1-77:66`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-params' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:56:1-77:66`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:56:1-77:66`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-params' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:56:1-77:66`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:56:1-77:66`)_

---

### #16 DECORATOR on middleware_decorator `wrap-file-info`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-file-info' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-file-info' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_

---

### #17 DECORATOR on middleware_decorator `wrap-cookies`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-cookies' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-cookies' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_

---

### #18 DECORATOR on middleware_decorator `wrap-content-type`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-content-type' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-content-type' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_

---

### #19 DECORATOR on middleware_decorator `wrap-file-prefer-files`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:35:1-42:42`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-file-prefer-files' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:35:1-42:42`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:35:1-42:42`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-file-prefer-files' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:35:1-42:42`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:35:1-42:42`)_

---

### #20 DECORATOR on middleware_decorator `wrap-file-prefer-handler`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:44:1-57:23`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-file-prefer-handler' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:44:1-57:23`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:44:1-57:23`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-file-prefer-handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:44:1-57:23`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:44:1-57:23`)_

---

### #21 DECORATOR on middleware_decorator `wrap-session`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-session' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-session' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_

---

### #22 DECORATOR on middleware_decorator `wrap-nested-params`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj:69:1-92:73`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-nested-params' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj:69:1-92:73`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj:69:1-92:73`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-nested-params' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj:69:1-92:73`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/nested_params.clj:69:1-92:73`)_

---

### #23 ADAPTER on protocol_adapter `String->StreamableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- **Summary:** Adapter pattern: adapts type 'String' to protocol 'StreamableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'String' to protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'String' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: write-body-to-stream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)

---

### #24 ADAPTER on protocol_adapter `clojure.lang.ISeq->StreamableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- **Summary:** Adapter pattern: adapts type 'clojure.lang.ISeq' to protocol 'StreamableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'clojure.lang.ISeq' to protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'clojure.lang.ISeq' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: write-body-to-stream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)

---

### #25 ADAPTER on protocol_adapter `java.io.InputStream->StreamableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- **Summary:** Adapter pattern: adapts type 'java.io.InputStream' to protocol 'StreamableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'java.io.InputStream' to protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'java.io.InputStream' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: write-body-to-stream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)

---

### #26 ADAPTER on protocol_adapter `java.io.File->StreamableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- **Summary:** Adapter pattern: adapts type 'java.io.File' to protocol 'StreamableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'java.io.File' to protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'java.io.File' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: write-body-to-stream, write-body-to-stream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)

---

### #27 ADAPTER on protocol_adapter `clojure.lang.IPersistentMap->p/Listener`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj)
- **Summary:** Adapter pattern: adapts type 'clojure.lang.IPersistentMap' to protocol 'p/Listener'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'clojure.lang.IPersistentMap' to protocol 'p/Listener' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'clojure.lang.IPersistentMap' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: on-open, on-message, on-pong, on-error, on-close _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj:3:1-18:48`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj:3:1-18:48`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj)

---

### #28 ADAPTER on protocol_adapter `clojure.lang.IPersistentMap->p/PingListener`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj)
- **Summary:** Adapter pattern: adapts type 'clojure.lang.IPersistentMap' to protocol 'p/PingListener'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'clojure.lang.IPersistentMap' to protocol 'p/PingListener' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'clojure.lang.IPersistentMap' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:8:1-24:30`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: on-ping _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj:20:1-27:66`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj:20:1-27:66`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-websocket-protocols/src/ring/websocket/protocols.clj)

---

### #29 ADAPTER on protocol_adapter `String->SizableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- **Summary:** Adapter pattern: adapts type 'String' to protocol 'SizableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'String' to protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'String' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: body-size-in-bytes _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)

---

### #30 ADAPTER on protocol_adapter `java.io.File->SizableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- **Summary:** Adapter pattern: adapts type 'java.io.File' to protocol 'SizableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'java.io.File' to protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'java.io.File' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: body-size-in-bytes _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)

---

### #31 ADAPTER on protocol_adapter `Object->SizableResponseBody`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- **Summary:** Adapter pattern: adapts type 'Object' to protocol 'SizableResponseBody'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'Object' to protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+30%** `[ADAPTER_EXTERNAL_TYPE_ADAPTATION]` Adapts external/standard host platform type 'Object' without modifying source class _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: body-size-in-bytes, body-size-in-bytes _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)

---

### #32 STRATEGY on protocol_strategy `StreamableResponseBody`
- **Confidence:** 82% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- **Summary:** Strategy pattern: protocol 'StreamableResponseBody' with 4 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'StreamableResponseBody' defines strategy interface with methods: write-body-to-stream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:7:1-13:62`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'String' implements strategy protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'clojure.lang.ISeq' implements strategy protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'java.io.InputStream' implements strategy protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'java.io.File' implements strategy protocol 'StreamableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj:55:1-80:28`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/src/ring/core/protocols.clj)

---

### #33 DECORATOR on middleware_decorator `make-blocking-service-method`
- **Confidence:** 79% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-blocking-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`)_

---

### #34 DECORATOR on middleware_decorator `make-async-service-method`
- **Confidence:** 79% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-async-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`)_

---

### #35 DECORATOR on middleware_decorator `make-blocking-service-method`
- **Confidence:** 79% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-blocking-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`)_

---

### #36 DECORATOR on middleware_decorator `make-async-service-method`
- **Confidence:** 79% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-async-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`)_
- **+45%** `[DECORATOR_RETURNS_CLOSURE]` Function returns an inner closure/function (fn [req ...] ...) decorating execution _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`)_

---

### #37 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-stacktrace`
- **Confidence:** 78% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-stacktrace' chains 3 middleware processing stages

#### 🔎 Evidence Trail:
- **+60%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 3 middleware handlers: wrap-stacktrace, wrap-stacktrace-log, wrap-stacktrace-web _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`)_

---

### #38 STRATEGY on multimethod_strategy `body-string`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:45:1-48:21`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)
- **Summary:** Strategy pattern: multimethod 'body-string' with 5 polymorphic dispatch strategies

#### 🔎 Evidence Trail:
- **+50%** `[STRATEGY_MULTIMETHOD_DECLARATION]` Multimethod dispatch definition '(defmulti body-string {:arglists '([request]) :added "1.2"})' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:45:1-48:21`)_
- **+45%** `[STRATEGY_DISPATCH_BRANCHES]` Found 5 distinct interchangeable strategy branches (defmethod): nil, String, clojure.lang.ISeq, java.io.File, java.io.InputStream _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:50:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:50:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:52:1-53:18`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:55:1-56:30`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:58:1-59:26`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj:61:1-62:26`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/request.clj)

---

### #39 STRATEGY on protocol_strategy `SizableResponseBody`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- **Summary:** Strategy pattern: protocol 'SizableResponseBody' with 3 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'SizableResponseBody' defines strategy interface with methods: body-size-in-bytes _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:4:1-10:16`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'String' implements strategy protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'java.io.File' implements strategy protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_
- **+20%** `[STRATEGY_EXTENSION_STRATEGY_IMPL]` Extension on 'Object' implements strategy protocol 'SizableResponseBody' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:19:1-30:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)

---

### #40 PROXY on proxy_factory_fn `make-output-stream`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:72:1-80:34`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Proxy pattern: 'make-output-stream' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'make-output-stream' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:72:1-80:34`)_

---

### #41 PROXY on proxy_factory_fn `servlet`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:130:1-138:52`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Proxy pattern: 'servlet' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:130:1-138:52`)_

---

### #42 PROXY on proxy_factory_fn `enumeration`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:15:1-19:63`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'enumeration' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'enumeration' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:15:1-19:63`)_

---

### #43 PROXY on proxy_factory_fn `async-context`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:21:1-23:43`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'async-context' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'async-context' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:21:1-23:43`)_

---

### #44 PROXY on proxy_factory_fn `servlet-request`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:25:1-45:61`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-request' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-request' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:25:1-45:61`)_

---

### #45 PROXY on proxy_factory_fn `servlet-response`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:47:1-65:54`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-response' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-response' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:47:1-65:54`)_

---

### #46 PROXY on proxy_factory_fn `servlet-config`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:67:1-69:32`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-config' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-config' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:67:1-69:32`)_

---

### #47 PROXY on proxy_factory_fn `defservice-test*`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:178:1-200:72`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Proxy pattern: 'defservice-test*' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'defservice-test*' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:178:1-200:72`)_

---

### #48 PROXY on proxy_factory_fn `http-servlet-request`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:7:1-31:81`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj)
- **Summary:** Proxy pattern: 'http-servlet-request' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'http-servlet-request' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:7:1-31:81`)_

---

### #49 PROXY on proxy_factory_fn `http-servlet-response`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:33:1-46:53`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj)
- **Summary:** Proxy pattern: 'http-servlet-response' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'http-servlet-response' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:33:1-46:53`)_

---

### #50 PROXY on proxy_factory_fn `make-output-stream`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:72:1-80:34`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Proxy pattern: 'make-output-stream' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'make-output-stream' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:72:1-80:34`)_

---

### #51 PROXY on proxy_factory_fn `servlet`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:130:1-138:52`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Proxy pattern: 'servlet' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:130:1-138:52`)_

---

### #52 PROXY on proxy_factory_fn `enumeration`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:14:1-18:63`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'enumeration' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'enumeration' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:14:1-18:63`)_

---

### #53 PROXY on proxy_factory_fn `async-context`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:20:1-22:43`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'async-context' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'async-context' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:20:1-22:43`)_

---

### #54 PROXY on proxy_factory_fn `servlet-request`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:24:1-44:61`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-request' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-request' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:24:1-44:61`)_

---

### #55 PROXY on proxy_factory_fn `servlet-response`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:46:1-64:54`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-response' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-response' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:46:1-64:54`)_

---

### #56 PROXY on proxy_factory_fn `servlet-config`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:66:1-68:32`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'servlet-config' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'servlet-config' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:66:1-68:32`)_

---

### #57 PROXY on proxy_factory_fn `defservice-test*`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:177:1-199:72`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Proxy pattern: 'defservice-test*' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'defservice-test*' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:177:1-199:72`)_

---

### #58 PROXY on proxy_factory_fn `output-stream-with-close-flag`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:62:1-70:36`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj)
- **Summary:** Proxy pattern: 'output-stream-with-close-flag' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'output-stream-with-close-flag' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:62:1-70:36`)_

---

### #59 PROXY on proxy_factory_fn `error-input-stream`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:72:1-77:61`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj)
- **Summary:** Proxy pattern: 'error-input-stream' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'error-input-stream' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:72:1-77:61`)_

---

### #60 PROXY on proxy_factory_fn `output-stream-with-flush-flag`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:100:1-110:37`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj)
- **Summary:** Proxy pattern: 'output-stream-with-flush-flag' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'output-stream-with-flush-flag' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core-protocols/test/ring/core/test/protocols.clj:100:1-110:37`)_

---

### #61 PROXY on proxy_factory_fn `file-upload`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:31:1-34:49`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj)
- **Summary:** Proxy pattern: 'file-upload' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'file-upload' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:31:1-34:49`)_

---

### #62 PROXY on proxy_factory_fn `proxy-handler`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:111:1-122:55`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj)
- **Summary:** Proxy pattern: 'proxy-handler' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'proxy-handler' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:111:1-122:55`)_

---

### #63 PROXY on proxy_factory_fn `async-proxy-handler`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:153:1-171:49`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj)
- **Summary:** Proxy pattern: 'async-proxy-handler' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'async-proxy-handler' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:153:1-171:49`)_

---

### #64 PROXY on proxy_factory_fn `chunked-stream-with-error`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:478:1-491:51`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- **Summary:** Proxy pattern: 'chunked-stream-with-error' generates surrogate proxy object wrapping target behavior

#### 🔎 Evidence Trail:
- **+70%** `[PROXY_NATIVE_PROXY_MACRO]` Function 'chunked-stream-with-error' instantiates a dynamic host proxy surrogate using (proxy ...) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:478:1-491:51`)_

---

### #65 ADAPTER on protocol_adapter `Duration->CookieInterval`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:87:1-90:36`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj)
- **Summary:** Adapter pattern: adapts type 'Duration' to protocol 'CookieInterval'

#### 🔎 Evidence Trail:
- **+65%** `[ADAPTER_EXTERNAL_PROTOCOL_EXTENSION]` Non-intrusive extension adapting type 'Duration' to protocol 'CookieInterval' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:87:1-90:36`)_
- **+20%** `[ADAPTER_ADAPTER_METHODS_IMPLEMENTED]` Provides protocol method implementations: ->seconds _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:53:1-54:21`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:53:1-54:21`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj)

---

### #66 FACADE on facade_namespace `ring.util.servlet`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Facade pattern: namespace 'ring.util.servlet' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.util.servlet' delegates calls to 3 distinct subsystems: Locale, string, protocols _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 3 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:1:1`)_

---

### #67 FACADE on facade_namespace `ring.bench.servlet`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj)
- **Summary:** Facade pattern: namespace 'ring.bench.servlet' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.bench.servlet' delegates calls to 3 distinct subsystems: java.util.Collections, servlet, jmh _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 3 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-bench/src/ring/bench/servlet.clj:1:1`)_

---

### #68 FACADE on facade_namespace `ring.middleware.stacktrace`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.stacktrace' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.stacktrace' delegates calls to 3 distinct subsystems: repl, io, st _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 5 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:1:1`)_

---

### #69 FACADE on facade_namespace `ring.util.jakarta.servlet`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Facade pattern: namespace 'ring.util.jakarta.servlet' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.util.jakarta.servlet' delegates calls to 3 distinct subsystems: Locale, string, protocols _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 3 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:1:1`)_

---

### #70 FACADE on facade_namespace `ring.websocket`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj)
- **Summary:** Facade pattern: namespace 'ring.websocket' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.websocket' delegates calls to 3 distinct subsystems: p, ByteBuffer, str _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 6 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/websocket.clj:1:1`)_

---

### #71 FACADE on facade_namespace `ring.middleware.resource`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.resource' provides unified interface over 5 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.resource' delegates calls to 5 distinct subsystems: codec, head, request, response _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:1:1`)_

---

### #72 FACADE on facade_namespace `ring.middleware.multipart-params`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.multipart-params' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.multipart-params' delegates calls to 3 distinct subsystems: req, parsing, IOUtils _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 4 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:1:1`)_

---

### #73 FACADE on facade_namespace `ring.middleware.file`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.file' provides unified interface over 5 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.file' delegates calls to 5 distinct subsystems: io, codec, head, request _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:1:1`)_

---

### #74 FACADE on facade_namespace `ring.middleware.session`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.session' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.session' delegates calls to 3 distinct subsystems: mem, store, cookies _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 5 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:1:1`)_

---

### #75 FACADE on facade_namespace `ring.util.response`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj)
- **Summary:** Facade pattern: namespace 'ring.util.response' provides unified interface over 4 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.util.response' delegates calls to 4 distinct subsystems: str, text, Thread, io _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 4 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:1:1`)_

---

### #76 FACADE on facade_namespace `ring.middleware.multipart-params.temp-file`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.multipart-params.temp-file' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.multipart-params.temp-file' delegates calls to 3 distinct subsystems: System, Runtime, io _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 3 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:1:1`)_

---

### #77 FACADE on facade_namespace `ring.middleware.session.cookie`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.session.cookie' provides unified interface over 6 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.session.cookie' delegates calls to 6 distinct subsystems: Mac, codec, Cipher, random _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 7 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj:1:1`)_

---

### #78 FACADE on facade_namespace `ring.middleware.test.cookies`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/cookies.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/cookies.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.test.cookies' provides unified interface over 3 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.test.cookies' delegates calls to 3 distinct subsystems: str, ZoneId, ZonedDateTime _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/cookies.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/cookies.clj:1:1`)_

---

### #79 FACADE on facade_namespace `ring.adapter.jetty`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj)
- **Summary:** Facade pattern: namespace 'ring.adapter.jetty' provides unified interface over 7 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.adapter.jetty' delegates calls to 7 distinct subsystems: wsp, ByteBuffer, ws, Duration _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 6 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:1:1`)_

---

### #80 FACADE on facade_namespace `ring.adapter.test.jetty`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- **Summary:** Facade pattern: namespace 'ring.adapter.test.jetty' provides unified interface over 4 subsystems

#### 🔎 Evidence Trail:
- **+55%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.adapter.test.jetty' delegates calls to 4 distinct subsystems: Thread, less-ssl, io, p _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 6 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:1:1`)_

---

### #81 STRATEGY on protocol_strategy `SessionStore`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/store.clj:4:1-21:63`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/store.clj)
- **Summary:** Strategy pattern: protocol 'SessionStore' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'SessionStore' defines strategy interface with methods: read-session, write-session, delete-session _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/store.clj:4:1-21:63`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'MemoryStore' provides concrete strategy implementation for protocol 'SessionStore' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/memory.clj:6:1-16:9`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'CookieStore' provides concrete strategy implementation for protocol 'SessionStore' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj:96:1-103:34`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/memory.clj:6:1-16:9`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/memory.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj:96:1-103:34`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session/cookie.clj)

---

### #82 DECORATOR on middleware_decorator `wrap-stacktrace`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-stacktrace' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-stacktrace' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:108:1-122:31`)_

---

### #83 DECORATOR on middleware_decorator `wrap-resource`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-resource' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-resource' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`)_

---

### #84 DECORATOR on middleware_decorator `wrap-file`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'wrap-file' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`)_
- **+35%** `[DECORATOR_MIDDLEWARE_NAMING]` Follows idiomatic Clojure/Ring middleware decorator naming convention 'wrap-file' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`)_

---

### #85 PROXY on virtual_proxy_state `default-store`
- **Confidence:** 74% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:88:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj)
- **Summary:** Virtual Proxy: lazy delay 'default-store' controls deferred access and instantiation of resource

#### 🔎 Evidence Trail:
- **+65%** `[PROXY_LAZY_DELAY_PROXY]` State 'default-store' creates a lazy virtual proxy using 'delay', deferring instantiation until accessed _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params.clj:88:1`)_

---

### #86 TEMPLATE_METHOD on template_bracket `wrap-stacktrace-log`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Template Method: 'wrap-stacktrace-log' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (handler, handler) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:14:1-36:29`)_

---

### #87 TEMPLATE_METHOD on template_bracket `wrap-stacktrace-web`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj)
- **Summary:** Template Method: 'wrap-stacktrace-web' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (handler) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/stacktrace.clj:92:1-106:48`)_

---

### #88 TEMPLATE_METHOD on template_bracket `do-every`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:11:1-16:37`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj)
- **Summary:** Template Method: 'do-every' encapsulates invariant algorithm/resource skeleton with customizable execution body

#### 🔎 Evidence Trail:
- **+45%** `[TEMPLATE_METHOD_TRY_FINALLY_BRACKET]` Encapsulates invariant resource safety skeleton (try/finally or try/catch) _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:11:1-16:37`)_
- **+35%** `[TEMPLATE_METHOD_CALLBACK_PARAMETER]` Accepts customizable callback parameter (body) executed inside template skeleton _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/multipart_params/temp_file.clj:11:1-16:37`)_

---

### #89 FACADE on facade_namespace `ring.handler.dump`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/handler/dump.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/handler/dump.clj)
- **Summary:** Facade pattern: namespace 'ring.handler.dump' provides unified interface over 2 subsystems

#### 🔎 Evidence Trail:
- **+45%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.handler.dump' delegates calls to 2 distinct subsystems: io, pprint _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/handler/dump.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/handler/dump.clj:1:1`)_

---

### #90 FACADE on facade_namespace `ring.middleware.params`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.params' provides unified interface over 2 subsystems

#### 🔎 Evidence Trail:
- **+45%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.params' delegates calls to 2 distinct subsystems: codec, req _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/params.clj:1:1`)_

---

### #91 FACADE on facade_namespace `ring.middleware.cookies`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.cookies' provides unified interface over 2 subsystems

#### 🔎 Evidence Trail:
- **+45%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.cookies' delegates calls to 2 distinct subsystems: str, codec _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 3 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:1:1`)_

---

### #92 FACADE on facade_namespace `ring.middleware.session.test.cookie`
- **Confidence:** 71% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:1:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj)
- **Summary:** Facade pattern: namespace 'ring.middleware.session.test.cookie' provides unified interface over 2 subsystems

#### 🔎 Evidence Trail:
- **+45%** `[FACADE_SUBSYSTEM_DELEGATION]` Namespace 'ring.middleware.session.test.cookie' delegates calls to 2 distinct subsystems: codec, Instant _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:1:1`)_
- **+30%** `[FACADE_UNIFIED_API_FUNCTIONS]` Provides 2 simplified unified façade wrapper functions _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:1:1`)_

---

### #93 STRATEGY on multimethod_strategy `resource-data`
- **Confidence:** 70% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:244:1-264:34`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj)
- **Summary:** Strategy pattern: multimethod 'resource-data' with 2 polymorphic dispatch strategies

#### 🔎 Evidence Trail:
- **+50%** `[STRATEGY_MULTIMETHOD_DECLARATION]` Multimethod dispatch definition '(defmulti resource-data {:arglists '([url]) :added "1.4"})' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:244:1-264:34`)_
- **+30%** `[STRATEGY_DISPATCH_BRANCHES]` Found 2 distinct interchangeable strategy branches (defmethod): :file, :jar _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:266:1-270:25`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:266:1-270:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj:292:1-298:58`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/util/response.clj)

---

### #94 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-resource`
- **Confidence:** 68% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-resource' chains 3 middleware processing stages

#### 🔎 Evidence Trail:
- **+60%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 3 middleware handlers: wrap-resource, wrap-resource-prefer-handler, wrap-resource-prefer-resources _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/resource.clj:48:1-73:69`)_

---

### #95 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-file`
- **Confidence:** 68% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-file' chains 3 middleware processing stages

#### 🔎 Evidence Trail:
- **+60%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 3 middleware handlers: wrap-file, wrap-file-prefer-files, wrap-file-prefer-handler _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file.clj:59:1-75:60`)_

---

### #96 FACTORY_METHOD on factory_function `make-blocking-service-method`
- **Confidence:** 67% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Factory pattern: constructor helper function 'make-blocking-service-method' creating structured domain objects

#### 🔎 Evidence Trail:
- **+35%** `[FACTORY_METHOD_FACTORY_NAMING]` Follows factory function naming convention 'make-blocking-service-method' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`)_
- **+40%** `[FACTORY_METHOD_CTOR_INVOCATION]` Invokes record constructor (->Type or map->Type) with default parameters/validation _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:99:1-105:51`)_

---

### #97 FACTORY_METHOD on factory_function `make-async-service-method`
- **Confidence:** 67% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Factory pattern: constructor helper function 'make-async-service-method' creating structured domain objects

#### 🔎 Evidence Trail:
- **+35%** `[FACTORY_METHOD_FACTORY_NAMING]` Follows factory function naming convention 'make-async-service-method' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`)_
- **+40%** `[FACTORY_METHOD_CTOR_INVOCATION]` Invokes record constructor (->Type or map->Type) with default parameters/validation _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:107:1-118:33`)_

---

### #98 FACTORY_METHOD on factory_function `make-blocking-service-method`
- **Confidence:** 67% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Factory pattern: constructor helper function 'make-blocking-service-method' creating structured domain objects

#### 🔎 Evidence Trail:
- **+35%** `[FACTORY_METHOD_FACTORY_NAMING]` Follows factory function naming convention 'make-blocking-service-method' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`)_
- **+40%** `[FACTORY_METHOD_CTOR_INVOCATION]` Invokes record constructor (->Type or map->Type) with default parameters/validation _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:99:1-105:51`)_

---

### #99 FACTORY_METHOD on factory_function `make-async-service-method`
- **Confidence:** 67% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Factory pattern: constructor helper function 'make-async-service-method' creating structured domain objects

#### 🔎 Evidence Trail:
- **+35%** `[FACTORY_METHOD_FACTORY_NAMING]` Follows factory function naming convention 'make-async-service-method' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`)_
- **+40%** `[FACTORY_METHOD_CTOR_INVOCATION]` Invokes record constructor (->Type or map->Type) with default parameters/validation _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:107:1-118:33`)_

---

### #100 FACTORY_METHOD on factory_function `create-threadpool`
- **Confidence:** 67% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:269:1-284:10`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj)
- **Summary:** Factory pattern: constructor helper function 'create-threadpool' creating structured domain objects

#### 🔎 Evidence Trail:
- **+35%** `[FACTORY_METHOD_FACTORY_NAMING]` Follows factory function naming convention 'create-threadpool' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:269:1-284:10`)_
- **+40%** `[FACTORY_METHOD_CTOR_INVOCATION]` Invokes record constructor (->Type or map->Type) with default parameters/validation _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:269:1-284:10`)_

---

### #101 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-reload`
- **Confidence:** 66% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-reload' chains 1 middleware processing stages

#### 🔎 Evidence Trail:
- **+40%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 1 middleware handlers: wrap-reload _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/src/ring/middleware/reload.clj:21:1-42:44`)_

---

### #102 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-file-info`
- **Confidence:** 66% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-file-info' chains 1 middleware processing stages

#### 🔎 Evidence Trail:
- **+40%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 1 middleware handlers: wrap-file-info _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/file_info.clj:58:1-79:25`)_

---

### #103 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-cookies`
- **Confidence:** 66% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-cookies' chains 1 middleware processing stages

#### 🔎 Evidence Trail:
- **+40%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 1 middleware handlers: wrap-cookies _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/cookies.clj:160:1-202:25`)_

---

### #104 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-content-type`
- **Confidence:** 66% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-content-type' chains 1 middleware processing stages

#### 🔎 Evidence Trail:
- **+40%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 1 middleware handlers: wrap-content-type _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_type.clj:23:1-43:25`)_

---

### #105 CHAIN_OF_RESPONSIBILITY on middleware_pipeline `wrap-session`
- **Confidence:** 66% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj)
- **Summary:** Chain of Responsibility: pipeline 'wrap-session' chains 1 middleware processing stages

#### 🔎 Evidence Trail:
- **+40%** `[CHAIN_OF_RESPONSIBILITY_MIDDLEWARE_CHAIN_CALLS]` Assembles pipeline chain of 1 middleware handlers: wrap-session _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_
- **+30%** `[CHAIN_OF_RESPONSIBILITY_THREADING_PIPELINE]` Uses threading pipeline (-> / ->>) to sequentially pass request context through chain stages _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/session.clj:78:1-119:31`)_

---

### #106 DECORATOR on middleware_decorator `make-service-method`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:120:1-128:46`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:120:1-128:46`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:120:1-128:46`)_

---

### #107 DECORATOR on middleware_decorator `defservice`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:140:1-158:57`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'defservice' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:140:1-158:57`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/src/ring/util/servlet.clj:140:1-158:57`)_

---

### #108 DECORATOR on middleware_decorator `run-servlet`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:71:1-78:46`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'run-servlet' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:71:1-78:46`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-servlet/test/ring/util/test/servlet.clj:71:1-78:46`)_

---

### #109 DECORATOR on middleware_decorator `is-lint-error`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/test/ring/middleware/test/lint.clj:31:1-32:62`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/test/ring/middleware/test/lint.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'is-lint-error' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/test/ring/middleware/test/lint.clj:31:1-32:62`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-devel/test/ring/middleware/test/lint.clj:31:1-32:62`)_

---

### #110 DECORATOR on middleware_decorator `make-service-method`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:120:1-128:46`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'make-service-method' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:120:1-128:46`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:120:1-128:46`)_

---

### #111 DECORATOR on middleware_decorator `defservice`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:140:1-158:57`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'defservice' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:140:1-158:57`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/src/ring/util/jakarta/servlet.clj:140:1-158:57`)_

---

### #112 DECORATOR on middleware_decorator `run-servlet`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:70:1-77:46`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'run-servlet' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:70:1-77:46`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jakarta-servlet/test/ring/util/jakarta/test/servlet.clj:70:1-77:46`)_

---

### #113 DECORATOR on middleware_decorator `body-size-in-bytes`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:25:3-26:16`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'body-size-in-bytes' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:25:3-26:16`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/src/ring/middleware/content_length.clj:25:3-26:16`)_

---

### #114 DECORATOR on middleware_decorator `trace-fn`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:13:1-19:23`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'trace-fn' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:13:1-19:23`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:13:1-19:23`)_

---

### #115 DECORATOR on middleware_decorator `trace`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:21:1-22:27`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'trace' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:21:1-22:27`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'f' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/test/session.clj:21:1-22:27`)_

---

### #116 DECORATOR on middleware_decorator `async-timeout-listener`
- **Confidence:** 62% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:143:1-151:26`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj)
- **Summary:** Decorator pattern: Ring-style middleware function 'async-timeout-listener' wrapping request handler

#### 🔎 Evidence Trail:
- **+40%** `[DECORATOR_HANDLER_PARAMETER]` Function accepts a wrapped handler parameter 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:143:1-151:26`)_
- **+30%** `[DECORATOR_DELEGATES_TO_HANDLER]` Explicitly delegates execution to the wrapped handler 'handler' _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/src/ring/adapter/jetty.clj:143:1-151:26`)_

---

### #117 SINGLETON on singleton_state `thread-exceptions`
- **Confidence:** 54% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:527:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- **Summary:** Singleton pattern: global state container 'thread-exceptions' initialized via atom

#### 🔎 Evidence Trail:
- **+35%** `[SINGLETON_STATEFUL_CONTAINER]` Holds mutable stateful reference container (atom) for global singleton state _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:527:1`)_
- **+25%** `[SINGLETON_ACCESSOR_FUNCTIONS]` Has 1 dedicated accessor/management functions: hello-world-cps-future _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:534:1-540:48`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:534:1-540:48`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)

---

### #118 SINGLETON on singleton_state `call-count`
- **Confidence:** 54% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:675:1`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- **Summary:** Singleton pattern: global state container 'call-count' initialized via atom

#### 🔎 Evidence Trail:
- **+35%** `[SINGLETON_STATEFUL_CONTAINER]` Holds mutable stateful reference container (atom) for global singleton state _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:675:1`)_
- **+25%** `[SINGLETON_ACCESSOR_FUNCTIONS]` Has 2 dedicated accessor/management functions: broken-handler, broken-handler-cps _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:677:1-679:45`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:677:1-679:45`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj:681:1-683:45`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-jetty-adapter/test/ring/adapter/test/jetty.clj)

---

### #119 STRATEGY on multimethod_strategy `print-method`
- **Confidence:** 36% (🔴 `LOW`)
- **Primary Location:** [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:63:1-64:59`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj)
- **Summary:** Strategy pattern: multimethod 'print-method' with 1 polymorphic dispatch strategies

#### 🔎 Evidence Trail:
- **+25%** `[STRATEGY_DISPATCH_BRANCHES]` Found 1 distinct interchangeable strategy branches (defmethod): Instant _(at `/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:63:1-64:59`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj:63:1-64:59`](/Volumes/External/Code/DPX/scratch/repos/ring/ring-core/test/ring/middleware/session/test/cookie.clj)

---
