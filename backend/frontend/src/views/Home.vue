<template>
  <div>
    <!-- Masthead-->
    <header class="masthead">
      <div class="container">
        <div class="masthead-heading text-uppercase">re:solve - die nachhaltige Lösung für Ihgr Unternehmen</div>
<!--        <div class="masthead-subheading">Welcome To Our Studio!</div>-->
        <router-link class="btn btn-primary btn-xl text-uppercase" :to="{ name: 'compareMaterial' }"
          >Materialien vergleichen</router-link
        >
      </div>
    </header>

    <!-- Über uns -->
    <section class="page-section" id="about">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Über uns</h2>
          <h3 class="section-subheading text-muted">
            re:solve ist ein Prototyp eines jungen Berliner Start-ups. Mit unserer Online-Webanwendung finden Sie mithilfe verschiedener Materialfilter
            und Öko-Index das passende Material für Ihren Bedarf.
            Unser Ziel ist es, qualitativ hochwertigen Service und umweltfreundliche Lösungen anzubieten. Dies wird durch unser qualifiziertes
            professionelles Team von freundlichen Mitarbeitern erreicht, deren Hauptziel es ist,
            Ihre Bedürfnisse zu befriedigen und die individuelle Lösung anzubieten.
          </h3>
        </div>
      </div>
    </section>

    <!-- Eco Score -->
    <section class="page-section" id="ecoscore">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Eco Score</h2>
          <h3 class="section-subheading text-muted">Der Eco-Score ist ein dynamischer Nachhaltigkeitsindex, der die Umweltfreundlichkeit verschiedener Materialien in direkten Vergleich stellt. Dabei werden Kriterien wie CO2-, Wasser- und Energieverbrauch, sowie die Recyclingfähigkeit berücksichtigt.Aus all diesen Nachhaltigkeitskriterien ergibt sich eine Skala, die Produkte von sehr gut bis ungenügend unterteilt. Ziel ist es Ihnen die Möglichkeit zu geben, die nachhaltigste Option für Ihr gewünschtes Material zu finden.</h3>
          <img
              src="@/assets/img/Eco_Score_Übersicht2.png"
              alt="..."
          />
          <p></p>

        </div>
      </div>
    </section>

    <!-- Portfolio Grid-->
    <!-- <section class="page-section bg-light" id="portfolio">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Portfolio</h2>
          <h3 class="section-subheading text-muted">
            Lorem ipsum dolor sit amet consectetur.
          </h3>
        </div>
        <div class="row">
          <div class="col-lg-4 col-sm-6 mb-4"> -->
            <!-- Portfolio item 1-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal1"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/1.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Threads</div>
                <div class="portfolio-caption-subheading text-muted">
                  Illustration
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 mb-4"> -->
            <!-- Portfolio item 2-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal2"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/2.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Explore</div>
                <div class="portfolio-caption-subheading text-muted">
                  Graphic Design
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 mb-4"> -->
            <!-- Portfolio item 3-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal3"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/3.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Finish</div>
                <div class="portfolio-caption-subheading text-muted">
                  Identity
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 mb-4 mb-lg-0"> -->
            <!-- Portfolio item 4-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal4"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/4.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Lines</div><section class="page-section" id="services">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Services</h2>
          <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
          <img>
            src="@/assets/img/team/Kate2_ret.jpg"
          </img>
        </div>
        </div>
      </div>
    </section>
                <div class="portfolio-caption-subheading text-muted">
                  Branding
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 mb-4 mb-sm-0"> -->
            <!-- Portfolio item 5-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal5"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/5.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Southwest</div>
                <div class="portfolio-caption-subheading text-muted">
                  Website Design
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6"> -->
            <!-- Portfolio item 6-->
            <!-- <div class="portfolio-item">
              <a
                class="portfolio-link"
                data-bs-toggle="modal"
                href="#portfolioModal6"
              >
                <div class="portfolio-hover">
                  <div class="portfolio-hover-content">
                    <i class="fas fa-plus fa-3x"></i>
                  </div>
                </div>
                <img
                  class="img-fluid"
                  src="@/assets/img/portfolio/6.jpg"
                  alt="..."
                />
              </a>
              <div class="portfolio-caption">
                <div class="portfolio-caption-heading">Window</div>
                <div class="portfolio-caption-subheading text-muted">
                  Photography
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section> -->
    <!-- About-->

<!--        <ul class="timeline">
          <li>
            <div class="timeline-image">
              <img
                class="rounded-circle img-fluid"
                src="@/assets/img/about/1.jpg"
                alt="..."
              />
            </div>
            <div class="timeline-panel">
              <div class="timeline-heading">
                <h4>2009-2011</h4>
                <h4 class="subheading">Our Humble Beginnings</h4>
              </div>
              <div class="timeline-body">
                <p class="text-muted">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt
                  ut voluptatum eius sapiente, totam reiciendis temporibus qui
                  quibusdam, recusandae sit vero unde, sed, incidunt et ea quo
                  dolore laudantium consectetur!
                </p>
              </div>
            </div>
          </li>
          <li class="timeline-inverted">
            <div class="timeline-image">
              <img
                class="rounded-circle img-fluid"
                src="@/assets/img/about/2.jpg"
                alt="..."
              />
            </div>
            <div class="timeline-panel">
              <div class="timeline-heading">
                <h4>March 2011</h4>
                <h4 class="subheading">An Agency is Born</h4>
              </div>
              <div class="timeline-body">
                <p class="text-muted">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt
                  ut voluptatum eius sapiente, totam reiciendis temporibus qui
                  quibusdam, recusandae sit vero unde, sed, incidunt et ea quo
                  dolore laudantium consectetur!
                </p>
              </div>
            </div>
          </li>
          <li>
            <div class="timeline-image">
              <img
                class="rounded-circle img-fluid"
                src="@/assets/img/about/3.jpg"
                alt="..."
              />
            </div>
            <div class="timeline-panel">
              <div class="timeline-heading">
                <h4>December 2015</h4>
                <h4 class="subheading">Transition to Full Service</h4>
              </div>
              <div class="timeline-body">
                <p class="text-muted">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt
                  ut voluptatum eius sapiente, totam reiciendis temporibus qui
                  quibusdam, recusandae sit vero unde, sed, incidunt et ea quo
                  dolore laudantium consectetur!
                </p>
              </div>
            </div>
          </li>
          <li class="timeline-inverted">
            <div class="timeline-image">
              <img
                class="rounded-circle img-fluid"
                src="@/assets/img/about/4.jpg"
                alt="..."
              />
            </div>
            <div class="timeline-panel">
              <div class="timeline-heading">
                <h4>July 2020</h4>
                <h4 class="subheading">Phase Two Expansion</h4>
              </div>
              <div class="timeline-body">
                <p class="text-muted">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt
                  ut voluptatum eius sapiente, totam reiciendis temporibus qui
                  quibusdam, recusandae sit vero unde, sed, incidunt et ea quo
                  dolore laudantium consectetur!
                </p>
              </div>
            </div>
          </li>
          <li class="timeline-inverted">
            <div class="timeline-image">
              <h4>
                Be Part
                <br />
                Of Our
                <br />
                Story!
              </h4>
            </div>
          </li>
        </ul>-->
    <!-- Team-->

    <!-- Hier sind einige der originalen Entwürfe auskommentiert man weiß ja nier wofür man es braucht
          Sie sollten wenn man es rückgängig macht wieder funktionieren ohne Störung-->

    <section class="page-section bg-light" id="team">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Team</h2>
          <h3 class="section-subheading text-muted">
            MENSCHEN HINTER UNSEREM ERFOLG
          </h3>
        </div>
        <div class="row">
          <div class="col-lg-4">
            <div class="team-member">
              <img
                class="mx-auto rounded-circle"
                src="@/assets/img/team/Paul_ret2.jpg"
                alt="..."
              />
              <h4>Paul Rensch</h4>
              <p class="text-muted">Teamleiter</p>
              <p class="text-muted">
                Paul ist ein echter Wegweiser für den Erfolg jedes Projekts. Unser Teamleiter ist dazu noch ein ausgezeichneter Kommunikator
                und für ihn ist die Zufriedenheit des Kunden sehr wichtig. Um Paul nicht zu verärgern, erledigen wir unsere Aufgaben noch vor
                dem gegebenen Deadline.
              </p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-twitter"></i-->
<!--              ></a>-->
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-facebook-f"></i-->
<!--              ></a>-->
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-linkedin-in"></i-->
<!--              ></a>-->
            </div>
          </div>
          <div class="col-lg-4">
            <div class="team-member">
              <img
                class="mx-auto rounded-circle"
                src="@/assets/img/team/Kate2_ret.jpg"
                alt="..."
              />
              <h4>Kateryna Hudovyk</h4>
              <p class="text-muted">Designerin und Frontend-Entwicklerin</p>
              <p class="text-muted">In Kate`s Freizeit von Reisen und Partys kreiert und verkörpert sie alle kreativen Ideen, beschäftigt
                sich mit der Erstellung unseres Webseiten-Designs, schreibt kreative Texte und inspiriert das gesamte Team.</p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-twitter"></i-->
<!--              ></a>-->
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-facebook-f"></i-->
<!--              ></a>-->
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"-->
<!--                ><i class="fab fa-linkedin-in"></i-->
<!--              ></a>-->
            </div>
          </div>
          <div class="col-lg-4">
            <div class="team-member">
              <img
                class="mx-auto rounded-circle"
                src="@/assets/img/team/Laura_ret.jpg"
                alt="..."
              />
              <h4>Laura Steinkemper</h4>
              <p class="text-muted">Projekt- und Qualitätsmanagerin, Fronend-Entwicklerin</p>
              <p class="text-muted">Laura überwacht, überprüft und optimiert alle unsere Schritte und macht so
                unser Team effektiv und erfolgsorientiert. Keine Bugs bleiben unbemerkt.  </p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"
                ><i class="fab fa-twitter"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
                ><i class="fab fa-facebook-f"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
                ><i class="fab fa-linkedin-in"></i
              ></a>-->
            </div>
          </div>
          <div class="col-lg-4">
            <div class="team-member">
              <img
                  class="mx-auto rounded-circle"
                  src="@/assets/img/team/Furkan_ret.jpg"
                  alt="..."
              />
              <h4>Furkan Öztürk</h4>
              <p class="text-muted">Projektmanager</p>
              <p class="text-muted">Das Leben als Projektmanager kann hart sein, aber nicht für Furkan. Unser Projektmanager ist wie eine Lokomotive, die unser Team stets vorwärts treibt.
                So gerne wie Goethe einst dichtete, erstellt Furkan seine wöchentliche Protokolle.</p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-twitter"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-facebook-f"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-linkedin-in"></i
              ></a>-->
            </div>
          </div>
          <div class="col-lg-4">
            <div class="team-member">
              <img
                  class="mx-auto rounded-circle"
                  src="@/assets/img/team/Jannes.jpg"
                  alt="..."
              />
              <h4>Jannes Lampe</h4>
              <p class="text-muted">Backend-Entwickler</p>
              <p class="text-muted">Jannes ist der Programmierer, der Programmiertrends kreiert. Er entwickelt und verbessert seine Programmierfähigkeiten ständig.
                Die Leidenschaft von Jannes hilft uns, die besten technischen Lösungen im Voraus bereitzustellen. </p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-twitter"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-facebook-f"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-linkedin-in"></i
              ></a>-->
            </div>
          </div>
          <div class="col-lg-4">
            <div class="team-member">
              <img
                  class="mx-auto rounded-circle"
                  src="@/assets/img/team/Leon.jpg"
                  alt="..."
              />
              <h4>Leon Boddin</h4>
              <p class="text-muted">Backend-Entwickler</p>
              <p>Leon ist ein Programmier-Guru. Leon versteht es, aus einem Traum eine technische Realität zu machen.
                Er hört immer zu und unterstützt das gesamte Team von der technischen Seite.</p>
<!--              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-twitter"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-facebook-f"></i
              ></a>
              <a class="btn btn-dark btn-social mx-2" href="#!"
              ><i class="fab fa-linkedin-in"></i
              ></a>-->
            </div>
          </div>
        </div>
<!--        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <p class="large text-muted">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut
              eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam
              corporis ea, alias ut unde.
            </p>
          </div>
        </div>-->
      </div>
    </section>

    <!-- Contact-->
    <section class="page-section" id="contact">
      <div class="container">
        <div class="text-center">
          <h2 class="section-heading text-uppercase">Kontaktiere uns</h2>
          <h3 class="section-subheading text-muted">

          </h3>
        </div>
        <!-- * * * * * * * * * * * * * * *-->
        <!-- * * SB Forms Contact Form * *-->
        <!-- * * * * * * * * * * * * * * *-->
        <!-- This form is pre-integrated with SB Forms.-->
        <!-- To make this form functional, sign up at-->
        <!-- https://startbootstrap.com/solution/contact-forms-->
        <!-- to get an API token!-->
        <form id="contactForm" data-sb-form-api-token="API_TOKEN">
          <div class="row align-items-stretch mb-5">
            <div class="col-md-6">
              <div class="form-group">
                <!-- Name input-->
                <input
                  class="form-control"
                  id="name"
                  type="text"
                  placeholder="Your Name *"
                  data-sb-validations="required"
                />
                <div class="invalid-feedback" data-sb-feedback="name:required">
                  A name is required.
                </div>
              </div>
              <div class="form-group">
                <!-- Email address input-->
                <input
                  class="form-control"
                  id="email"
                  type="email"
                  placeholder="Your Email *"
                  data-sb-validations="required,email"
                />
                <div class="invalid-feedback" data-sb-feedback="email:required">
                  An email is required.
                </div>
                <div class="invalid-feedback" data-sb-feedback="email:email">
                  Email is not valid.
                </div>
              </div>
              <div class="form-group mb-md-0">
                <!-- Phone number input-->
                <input
                  class="form-control"
                  id="phone"
                  type="tel"
                  placeholder="Your Phone *"
                  data-sb-validations="required"
                />
                <div class="invalid-feedback" data-sb-feedback="phone:required">
                  A phone number is required.
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group form-group-textarea mb-md-0">
                <!-- Message input-->
                <textarea
                  class="form-control"
                  id="message"
                  placeholder="Your Message *"
                  data-sb-validations="required"
                ></textarea>
                <div
                  class="invalid-feedback"
                  data-sb-feedback="message:required"
                >
                  A message is required.
                </div>
              </div>
            </div>
          </div>
          <!-- Submit success message-->
          <!---->
          <!-- This is what your users will see when the form-->
          <!-- has successfully submitted-->
          <div class="d-none" id="submitSuccessMessage">
            <div class="text-center text-white mb-3">
              <div class="fw-bolder">Form submission successful!</div>
              To activate this form, sign up at
              <br />
              <a href="https://startbootstrap.com/solution/contact-forms"
                >https://startbootstrap.com/solution/contact-forms</a
              >
            </div>
          </div>
          <!-- Submit error message-->
          <!---->
          <!-- This is what your users will see when there is-->
          <!-- an error submitting the form-->
          <div class="d-none" id="submitErrorMessage">
            <div class="text-center text-danger mb-3">
              Error sending message!
            </div>
          </div>
          <!-- Submit Button-->
          <div class="text-center">
            <button
              class="btn btn-primary btn-xl text-uppercase disabled"
              id="submitButton"
              type="submit"
            >
              Send Message
            </button>
          </div>
        </form>
      </div>
    </section>


    <!-- Footer-->
    <footer class="footer py-4">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-4 text-lg-start">Copyright &copy; re:solve</div>
          <div class="col-lg-4 my-3 my-lg-0">
            <a class="link-dark text-decoration-none me-3" href="#!">Impressum: </a>
            <a class="link-dark text-decoration-none" href="#!">Wilhelminenhofstr. 75A 12459 Berlin</a>
          </div>
          <div class="col-lg-4 text-lg-end">
            <a class="link-dark text-decoration-none" href="#!">Tel: +49 183 12 29 169 / </a>
            <a class="link-dark text-decoration-none" href="#!">E-Mail: genimatics@gmail.com</a>
          </div>
        </div>
      </div>
    </footer>












  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      materials: [],
    };
  },
  // methods: {
  //   async getMaterials() {
  //     let endpoint = "/api/materials/";
  //     try {
  //       const response = await axios.get(endpoint);
  //       this.materials = response.data;
  //     } catch (error) {
  //       console.log(error.response);
  //       alert(error.response.statustext);
  //     }
  //   },
  // },
  // created() {
  //   this.getMaterials();
  // },
};
</script>
