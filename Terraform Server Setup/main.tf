provider "google" {
  credentials = file("<CREDENTIALS_JSON_FILE>")
  project     = "<YOUR_PROJECT_ID>"
  region      = "us-central1"
}

resource "google_compute_instance" "default" {
  name         = "flask-app-instance"
  machine_type = "e2-small"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }

  metadata_startup_script = file("startup-script.sh")
}
