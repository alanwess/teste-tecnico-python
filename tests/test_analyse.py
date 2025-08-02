from fastapi.testclient import TestClient
from app.main import app
import io
from PIL import Image, ImageDraw, ImageFont

client = TestClient(app)

def test_summarization():
    fake_pdf = io.BytesIO(b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\nxref\n0 1\n0000000000 65535 f\ntrailer\n<<>>\nstartxref\n0\n%%EOF")
    files = [("files", ("sample.pdf", fake_pdf, "application/pdf"))]
    data = {
        "request_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "test_user"
    }
    response = client.post("/v1/analyse", files=files, data=data)
    assert response.status_code == 200
    assert "summary" in response.json()

def test_qa_with_query_jpg():
    img = Image.new("RGB", (400, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    texto = "Alan é engenheiro de software"

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    draw.text((10, 40), texto, fill=(0, 0, 0), font=font)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    files = [("files", ("sample.jpg", img_bytes, "image/jpeg"))]
    data = {
        "request_id": "00000000-0000-0000-0000-000000000001",
        "user_id": "test_user",
        "query": "Qual é a profissão de Alan?"
    }

    response = client.post("/v1/analyse", files=files, data=data)
    assert response.status_code == 200
    assert "responses" in response.json()