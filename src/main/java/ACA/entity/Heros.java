package ACA.entity;

    import com.baomidou.mybatisplus.annotation.IdType;
    import com.baomidou.mybatisplus.annotation.TableId;
    import java.io.Serializable;
    import lombok.Data;
    import lombok.EqualsAndHashCode;
    import lombok.experimental.Accessors;

/**
* <p>
    * 
    * </p>
*
* @author tiebiao Z
* @since 2020-03-14
*/
    @Data
        @EqualsAndHashCode(callSuper = false)
    @Accessors(chain = true)
    public class Heros implements Serializable {

    private static final long serialVersionUID = 1L;

            @TableId(value = "hero_id", type = IdType.AUTO)
    private Integer heroId;

    private String heroName;

    private String heroFetters;

    private Integer cost;


}