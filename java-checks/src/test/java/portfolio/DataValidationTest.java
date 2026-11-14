package portfolio;
import java.io.File;
import org.apache.metamodel.csv.CsvDataContext;
import org.apache.metamodel.data.DataSet;
import org.apache.metamodel.schema.Table;
import org.testng.Assert;
import org.testng.annotations.Test;
public class DataValidationTest {
 @Test public void querySyntheticCsvWithMetaModel() {
  CsvDataContext context = new CsvDataContext(new File("data/synthetic.csv"));
  Table table = context.getDefaultSchema().getTables().get(0);
  int count = 0;
  try (DataSet data = context.query().from(table).selectAll().execute()) {
   while(data.next()) { Assert.assertNotNull(data.getRow().getValue(0)); count++; }
  }
  Assert.assertEquals(count, 2);
 }
}
