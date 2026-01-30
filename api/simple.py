from django.http import HttpResponse

def handler(request, context=None):
    """
    Simple static version of ECHOGA Foundation homepage
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ECHOGA Foundation - Empowering Communities</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            .hero-section {
                background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                color: white;
            }
            .text-gold { color: #FFD700; }
            .founder-image {
                border: 5px solid #FFD700;
                border-radius: 50%;
                width: 250px;
                height: 250px;
                object-fit: cover;
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color: #1B5E20;">
            <div class="container">
                <a class="navbar-brand d-flex align-items-center" href="#">
                    <img src="https://res.cloudinary.com/dafag8jhg/image/upload/w_40,h_40/echoga_foundation/images/logo.jpg" alt="ECHOGA Foundation Logo" width="40" height="40">
                    <span class="ms-2">ECHOGA</span>
                    <img src="https://res.cloudinary.com/dafag8jhg/image/upload/w_35,h_35,c_fill,g_face/echoga_foundation/images/founder.jpg" alt="Hon. Ismaila Muhammed Attah" 
                         class="rounded-circle ms-2" width="35" height="35" style="border: 2px solid #FFD700;">
                </a>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="hero-section">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <h1 class="display-3 mb-4">ECHOGA Foundation</h1>
                        <p class="lead mb-3">Founded by <strong>Hon. Ismaila Muhammed Attah</strong></p>
                        <p class="lead mb-3 text-gold">Supervising Councillor, Ankpa LGA</p>
                        <p class="lead mb-4">Empowering Communities, Transforming Lives, Building a Better Nigeria</p>
                        <div class="hero-buttons">
                            <a href="#about" class="btn btn-warning btn-lg me-3">Meet Our Founder</a>
                        </div>
                    </div>
                    <div class="col-lg-4 text-center">
                        <div class="hero-founder-image">
                            <img src="https://res.cloudinary.com/dafag8jhg/image/upload/w_250,h_250,c_fill,g_face/echoga_foundation/images/founder-1.jpg" 
                                 alt="Hon. Ismaila Muhammed Attah" class="founder-image shadow-lg">
                            <div class="mt-3">
                                <h5>Hon. Ismaila Muhammed Attah</h5>
                                <p class="text-gold mb-0">Founder & Chairman</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section class="py-5" id="about" style="background-color: #f8f9fa;">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-5 mb-4 mb-lg-0">
                        <img src="https://res.cloudinary.com/dafag8jhg/image/upload/w_400,h_300,c_fill,g_face/echoga_foundation/images/founder-2.jpg" 
                             alt="Hon. Ismaila Muhammed Attah" class="img-fluid rounded shadow">
                    </div>
                    <div class="col-lg-7">
                        <h3 class="mb-3">Hon. Ismaila Muhammed Attah</h3>
                        <p class="lead text-warning mb-2">Founder & Chairman, ECHOGA Foundation</p>
                        <p class="lead text-success mb-3">Supervising Councillor, Ankpa LGA</p>
                        <p>Hon. Ismaila Muhammed Attah, popularly known as <strong>Echoga</strong>, is a distinguished leader,
                            philanthropist, and community development advocate dedicated to transforming lives across Nigeria.</p>
                        <p>Currently serving as the Supervising Councillor of Ankpa Local Government Area, Hon. Attah combines his political leadership with philanthropic work to create meaningful change in communities.</p>
                        <p>With unwavering commitment to social justice and sustainable development, Hon. Attah has dedicated
                            his life to creating opportunities for the less privileged through education, healthcare, youth
                            empowerment, and community development initiatives.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="py-4" style="background-color: #1B5E20; color: white;">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4">
                        <div class="d-flex align-items-start mb-3">
                            <img src="https://res.cloudinary.com/dafag8jhg/image/upload/w_60,h_60,c_fill,g_face/echoga_foundation/images/founder-1.jpg" 
                                 alt="Hon. Ismaila Muhammed Attah" class="rounded-circle me-3" width="60" height="60">
                            <div>
                                <h5 class="text-warning mb-1">About ECHOGA Foundation</h5>
                                <small>Founded by Hon. Ismaila Muhammed Attah</small>
                            </div>
                        </div>
                        <p>ECHOGA Foundation is dedicated to empowering communities through education, healthcare, youth development, and sustainable community initiatives across Nigeria.</p>
                        <p class="mb-0"><em>"Your Progress, Our Commitment!"</em></p>
                    </div>
                    <div class="col-lg-8">
                        <div class="text-center">
                            <p>&copy; 2024 ECHOGA Foundation. All rights reserved. | Empowering Communities, Transforming Lives</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return HttpResponse(html_content, content_type='text/html')