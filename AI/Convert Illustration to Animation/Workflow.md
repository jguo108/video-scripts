This is the "Preservation Workflow." This is distinct from the previous workflows because your goal is now **restoration and augmentation**, not creation.

The biggest technical challenge you will face is **"The Floating Text Problem."** If you feed a page with text directly into a video AI (Veo), the letters will warp, melt, and float around, which looks nightmarish.

**The Strategy:** We must surgically remove the text from your illustrations, animate the "clean" art, and then put the text back as live HTML code.

Here is the workflow to keep the original art but make it alive.

---

### **Phase 1: Extraction (Gemini 3)**

**Goal:** Get the text out of the PDF so you have a digital copy of the script.

The Prompt:

Upload the PDF.

> "I am converting this specific PDF book into a web app. I need to extract the text.
> 
> Please create a structured list (JSON format preferred) where each item represents a page.
> 
> Format:
> 
> { "page": 1, "text": "Extracted text..." }
> 
> **Crucial:** Please double-check the OCR accuracy against the original images. Do not summarize; extract word-for-word."

---

### **Phase 2: The "Clean Plate" (Nano Banana)**

Goal: Create a version of your original illustration without the text.

We use Nano Banana's "Inpainting" or "Edit" capabilities here. We are not asking it to draw a new image; we are asking it to "heal" the image where the text used to be.

The Prompt (Nano Banana / Gemini Image Editor):

Upload a screenshot of one specific page.

> "Task: Remove Text / Inpaint.
> 
> Instructions: Identify the text overlay on this image and remove it. Fill in the empty space to perfectly match the existing background texture and art style.
> 
> Constraint: Do not change the character design, colors, or art style. Leave the rest of the image exactly as it is. I only want the text gone."

_Note: If your book has the text on a white page separate from the illustration, you can skip this step and just crop the image! This step is only if the text is ON top of the art._

---

### **Phase 3: Animation (Veo 3)**

Goal: Make the original art move.

Since you want to keep the original style, you must lower the "creativity" or "hallucination" settings of the video model to ensure it doesn't turn your 2D drawing into a 3D movie.

The Prompt (Veo 3):

Upload the "Clean" image from Phase 2.

> "Input: [Clean Image]
> 
> Prompt: Gently animate this scene. A slight breeze moves the [trees/hair/clouds]. Keep the camera locked (static tripod).
> 
> Style Preservation: Maintain the original 2D illustration style strictly. Do not convert to 3D or photorealism.
> 
> Motion Strength: Low/Subtle. (High motion risks warping the original art)."

---

### **Phase 4: The Reassembly (Gemini 3 Coding)**

**Goal:** Build the "sandwich": The animated video at the back, and the extracted text at the front.

**The Prompt (Gemini 3):**

> "I am ready to build the app.
> 
> 1. **Assets:** rep.
>     
> 2. **Data:** I have the JSON text you extracted in Phase 1.
>     
> 
> Please a Storybook Web App**.
> 
> **Requirements:**
> 
> - **Background:** Full-screen video that autoplays/loops.
>     
> - **Foreground:** The text from the JSON should appear at the bottom center.
>     
> - **Styling:** The text should have a 'frosted glass' background effect (blur backdrop-filter) so it is readable against the moving video. Use a font that matches the vibe of a children's book (like 'Quicksand' or 'Comfortaa' from Google Fonts).
> - ** Styling**: Words of the text should appear and disappear as they are read out. Use a font that matches the vibe of a children's book (like 'Quicksand' or 'Comfortaa' from Google Fonts). Text should be display at the top of each scene.
>     
> - **Navigation:** Arrow keys or swipe to change pages.
> - **Voice over**: As the video plays, reads the text slowly. Use a female voice that sounds like a kindergarten teacher"
>     

---

### **Summary of the "Preservation" Prompts**

| **Tool**        | **Role**        | **The "Secret Sauce" in the Prompt**                                                               |
| --------------- | --------------- | -------------------------------------------------------------------------------------------------- |
| **Gemini 3**    | **OCR Scanner** | _"Extract word-for-word. Output as JSON."_                                                         |
| **Nano Banana** | **Restorer**    | _"**Task: Inpaint.** Remove the text. **Constraint:** Do not change the art style or characters."_ |
| **Veo 3**       | **Animator**    | _"**Motion Strength: Low.** Maintain 2D illustration style. Do not convert to 3D."_                |
| **Gemini 3**    | **Publisher**   | _"Overlay the text on a 'frosted glass' div so it floats above the video."_                        |

### **A Technical Note on "Nano Banana" for Editing**

If the standard generation prompt changes your art too much (e.g., it makes the toaster look different), you should look for the specific **"Edit"** or **"Inpaint"** mode in the interface.

If you are using a chat interface that doesn't have a specific "Edit button," use this prompt text:

> "Edit this image. Mask out the text area. Regenerate the masked area to match the surrounding background pattern."

**Would you like to try a test on the first page? You can paste the text from Page 1 here, and describe the illustration, and I can give you the exact Veo prompt to make that specific illustration move safely.**