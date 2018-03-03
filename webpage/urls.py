from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  # Main
  path("", views.index, name="index"),
  # Contact
  path("contact", views.contact, name="contact"),
  # Thanks
  path("thanks", views.thanks, name="thanks"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# f = []
# for i in range(0, 12):
#  f.append(cv2.imread("tmp{}.jpg".format(i)))
# holder = np.zeros([3096, 4128, 3], np.uint8)
# holder[:1032, :1032, :] = f[0]
# holder[:1032, 1032:2064, :] = f[1]
# holder[:1032, 2064:3096, :] = f[2]
# holder[:1032, 3096:4128, :] = f[3]
# holder[1032:2064, :1032, :] = f[4]
# holder[1032:2064, 1032:2064, :] = f[5]
# holder[1032:2064, 2064:3096, :] = f[6]
# holder[1032:2064, 3096:4128, :] = f[7]
# holder[2064:3096, :1032, :] = f[8]
# holder[2064:3096, 1032:2064, :] = f[9]
# holder[2064:3096, 2064:3096, :] = f[10]
# holder[2064:3096, 3096:4128, :] = f[11]
# cv2.imwrite("diagnosed.jpg", holder)
